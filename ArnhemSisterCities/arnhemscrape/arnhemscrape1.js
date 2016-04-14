// terminal: node arnhemscrape.js

var request = require('request');
var cheerio = require('cheerio');
var fs = require('fs');

var base = "http://nl.wikipedia.org";
var site = base + "/wiki/Arnhem";

var date = new Date().toString();
var filename = "arnhem_tree_" + date + ".txt";

var file = fs.createWriteStream(filename);
var unique = fs.createWriteStream(filename.replace('.txt', '$unique.txt'));

var level = 0;
var visited = [];

process.stdin.resume();
process.on('SIGINT', function() {
    unique.write(visited.join('\n'));
    process.exit();
});

var getPage = function(uri, prev) {
    file.write(prev + '\n');
    console.log(prev);

    request(uri, function(error, response, body) {
        if (!error && response.statusCode == 200) {
            $ = cheerio.load(body);
            
            names = 0;
            if(names == 0) names = $('h2:has(#Stedenbanden) + p + ul li a:last-child').toArray();
            if(names == 0) names = $('h2:has(#Stedenbanden) + ul li a:last-child').toArray();
            if(names == 0) names = $('h2:has(#Partnersteden) + p + ul li a:last-child').toArray();
            if(names == 0) names = $('h2:has(#Partnersteden) + ul li a:last-child').toArray();
            if(names == 0) names = $('h2:has(#Zustersteden) + p + ul li a:last-child').toArray();
            if(names == 0) names = $('h2:has(#Zustersteden) + ul li a:last-child').toArray();

            var partners = [];
            names.forEach(function(name) {
                name.children.forEach(function(child) {
                    partners.push({
                        name: child.data,
                        url: child.parent.attribs.href
                    });
                });
            });

            partners.forEach(function(partner) {
                var accept = true;
                visited.forEach(function(visit) {
                    if(visit == partner.name) accept = false;
                });

                if(accept) {
                    visited.push(partner.name);
                    getPage(base + partner.url, prev + ' > ' + partner.name);
                }
            });
        }
    })
}

getPage(site, 'Arnhem');