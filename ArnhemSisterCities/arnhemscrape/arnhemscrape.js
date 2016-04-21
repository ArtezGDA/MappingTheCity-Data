// terminal: node arnhemscrape.js

var request = require('request');
var cheerio = require('cheerio');
var geocoder = require('geocoder');
var fs = require('fs');

var base = "http://nl.wikipedia.org";
var site = base + "/wiki/Arnhem";

var date = new Date().toString();
var filename = "arnhem_tree_" + date + ".txt";

var tree = { city: 'Arnhem', children: [] };
var visited = [];

var json = fs.createWriteStream('arnhemtree_'+date+'.json')


// 1 X CTRL-C DRUKKEN OM JSON OP TE SLAAN (en even wachten)
process.stdin.resume();
process.on('SIGINT', function() {
    json.write(JSON.stringify(tree, null, 4));
    process.exit();
});

var cityObject = function(city, partners, coords) {
    return {
        city: city,
        partners: partners,
        coords: coords
    }
};

var getPage = function(uri, prev) {
    
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
                    var coords = '';
                    geocoder.geocode(partner.name, function(err, data) {
                        if(data && data.results.length) {
                            coords = data.results[0].geometry.location;

                            // MET COORDINATEN

                            // visited.push(partner.name);
                            // var partnerObject = { city: partner.name, coords: coords, children: [] } 
                            // prev.children.push(partnerObject)
                            // getPage(base + partner.url, partnerObject);
                        }
                    });

                    // ZONDER COORDINATEN

                    visited.push(partner.name);
                    var partnerObject = { city: partner.name, children: [] } 
                    prev.children.push(partnerObject)
                    getPage(base + partner.url, partnerObject);
                }
            });

            console.log(tree);
        }
    });
}

getPage(site, tree);