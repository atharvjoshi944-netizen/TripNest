"""
Showcase pre-loaded trips for instant exploration and offline testing.
Platform ID: 6ac33976fb8fc7965cd9236d
"""

SHOWCASE_TRIPS = [
    {
        "id": "kyoto-zen-01",
        "title": "Kyoto Cultural Immersion & Ancient Zen",
        "destination": "Kyoto, Japan",
        "duration": 5,
        "start_date": "2026-11-10",
        "end_date": "2026-11-14",
        "budget_tier": "Moderate ($$/₹₹)",
        "party_type": "Couple / Romantic",
        "pace": "Moderate",
        "currency": "USD ($)",
        "created_at": "2026-10-26 14:30",
        "estimated_total_cost": 890.0,
        "vibe_tag": "Cultural & Historic Heritage",
        "transit_summary": "Intelligent geographic clustering: West Arashiyama (Day 1) -> South Fushimi & Gion (Day 2) -> North Zen Belt (Day 3) -> East Higashiyama (Day 4) -> Nara Excursion (Day 5). Average transit < 15 mins.",
        "days": [
            {
                "day_number": 1,
                "title": "Bamboo Whispers & Western Arashiyama Sanctuary",
                "cluster_zone": "Western Kyoto (Arashiyama & Sagano)",
                "transit_fatigue_score": "Low (95% transit efficiency - all walkable)",
                "transit_notes": "Take JR Sagano line to Saga-Arashiyama; entire day explored on foot along the Oi River.",
                "slots": {
                    "morning": {
                        "time": "08:30 - 11:30",
                        "title": "Arashiyama Bamboo Grove & Tenryu-ji Zen Temple",
                        "description": "Walk through soaring bamboo stalks early before crowds, followed by the UNESCO-listed 14th-century Sogenchi garden.",
                        "estimated_cost": 15.0,
                        "vibe": "Zen & Nature",
                        "tips": "Arrive before 9:00 AM for undisturbed photos and serene soundscape."
                    },
                    "lunch": {
                        "time": "12:00 - 13:30",
                        "title": "Shigetsu Buddhist Temple Vegetarian Cuisine (Shojin Ryori)",
                        "description": "Exquisite seasonal vegan multi-course meal prepared by Zen monks inside Tenryu-ji grounds overlooking pine gardens.",
                        "estimated_cost": 32.0,
                        "vibe": "Culinary Heritage",
                        "tips": "Advance booking recommended; shoe removal required at entrance."
                    },
                    "afternoon": {
                        "time": "14:00 - 17:00",
                        "title": "Sagano Romantic Train & Okochi Sanso Villa",
                        "description": "Heritage diesel train ride along the emerald Hozugawa River gorge, followed by the tranquil hillside villa of silent film star Denjiro Okochi.",
                        "estimated_cost": 22.0,
                        "vibe": "Scenic & Historical",
                        "tips": "Okochi ticket includes complimentary matcha and sweet treat in tea pavilion."
                    },
                    "evening": {
                        "time": "18:00 - 21:00",
                        "title": "Togetsukyo Bridge Sunset & Riverside Kaiseki",
                        "description": "Golden hour stroll across the iconic Moon Crossing Bridge and traditional riverside Kaiseki dinner tasting Kyoto yuba (tofu skin).",
                        "estimated_cost": 65.0,
                        "vibe": "Romantic Dining",
                        "tips": "Try local Kyoto craft beers (Matcha IPA) at the riverside terrace."
                    }
                },
                "day_cost": 134.0
            },
            {
                "day_number": 2,
                "title": "Torii Gates & Lantern-Lit Geisha Alleys",
                "cluster_zone": "Southern & Eastern Kyoto (Fushimi & Gion)",
                "transit_fatigue_score": "Minimal (Direct Keihan train link, zero backtracking)",
                "transit_notes": "Keihan Main Line connects Fushimi Inari directly to Gion-Shijo in 12 minutes.",
                "slots": {
                    "morning": {
                        "time": "08:00 - 11:30",
                        "title": "Fushimi Inari Taisha Thousand Vermilion Torii Gates",
                        "description": "Climb through the mountain tunnel of 10,000 crimson gates dedicated to the Shinto deity of harvest and foxes.",
                        "estimated_cost": 0.0,
                        "vibe": "Iconic Spiritual",
                        "tips": "Hike up to Yotsutsuji intersection for panoramic views of southern Kyoto."
                    },
                    "lunch": {
                        "time": "12:15 - 13:45",
                        "title": "Kitsune Udon & Inari Sushi at Kendonya",
                        "description": "Handmade chewy udon served with sweet fried tofu skin broth, a local specialty of Fushimi.",
                        "estimated_cost": 16.0,
                        "vibe": "Comfort Food",
                        "tips": "Cash only; ask for spicy Kyoto shichimi pepper on the side."
                    },
                    "afternoon": {
                        "time": "14:15 - 17:30",
                        "title": "Kennin-ji Dragon Ceiling & Historic Hanami-koji Street",
                        "description": "Kyoto's oldest Zen temple featuring the twin dragon ceiling painting, followed by strolling through preserved 17th-century wooden tea houses.",
                        "estimated_cost": 12.0,
                        "vibe": "Living Heritage",
                        "tips": "Do not photograph working geiko/maiko directly; observe respectful etiquette."
                    },
                    "evening": {
                        "time": "18:30 - 21:30",
                        "title": "Pontocho Alley Izakaya Crawl & Kamogawa River Stroll",
                        "description": "Explore the narrow cobblestone alley lined with lanterns, tasting yakitori skewers and seasonal sake alongside the cooling river.",
                        "estimated_cost": 55.0,
                        "vibe": "Nightlife & Gastro",
                        "tips": "Sit on the Kamogawa riverbank after dinner with locals for a relaxing breeze."
                    }
                },
                "day_cost": 83.0
            },
            {
                "day_number": 3,
                "title": "Golden Splendor, Rock Gardens & Foodie Alleys",
                "cluster_zone": "North-Central Kyoto (Kinukake-no-Michi Belt)",
                "transit_fatigue_score": "High Optimization (Walkable heritage path along foot of Mt. Kinugasa)",
                "transit_notes": "Bus #205 connects Golden Pavilion to Ryoan-ji in 6 mins, then subway straight to Nishiki Market.",
                "slots": {
                    "morning": {
                        "time": "09:00 - 12:00",
                        "title": "Kinkaku-ji (Golden Pavilion) & Ryoan-ji Rock Garden",
                        "description": "Marvel at the top two floors covered in pure gold leaf reflecting in the Kyoko-chi pond, followed by the world's most famous 15-stone Zen riddle garden.",
                        "estimated_cost": 14.0,
                        "vibe": "Architectural Wonder",
                        "tips": "Count the stones from the veranda; only 14 can be seen from any single angle!"
                    },
                    "lunch": {
                        "time": "12:30 - 14:00",
                        "title": "Nishiki Market Culinary Safari",
                        "description": "Graze through 'Kyoto's Kitchen' tasting freshly grilled wagyu skewers, tamagoyaki omelet, and sesame dango.",
                        "estimated_cost": 24.0,
                        "vibe": "Street Gastronomy",
                        "tips": "Stand inside the shop stalls to eat as street eating while walking is discouraged."
                    },
                    "afternoon": {
                        "time": "14:30 - 17:30",
                        "title": "Kyoto Imperial Palace Grounds & Tea Ceremony Workshop",
                        "description": "Walk the tranquil gravel avenues of the imperial residence and participate in an authentic Urasenke matcha whisking ritual.",
                        "estimated_cost": 35.0,
                        "vibe": "Cultural Masterclass",
                        "tips": "Palace gardens are free; tea workshop includes confectionery tasting."
                    },
                    "evening": {
                        "time": "18:30 - 21:30",
                        "title": "Dinner at Gion Duck Noodles & Craft Cocktail Bar Rocking Chair",
                        "description": "Modern duck ramen hidden behind an emoji sign, finished with world-class mixology by award-winning bartenders beside an antique fireplace.",
                        "estimated_cost": 50.0,
                        "vibe": "Cocktails & Dining",
                        "tips": "Order the Smoked Duck Ramen with dipping tsukemen broth."
                    }
                },
                "day_cost": 123.0
            },
            {
                "day_number": 4,
                "title": "Terrace Views & Preservation Alleys of Higashiyama",
                "cluster_zone": "Eastern Hillside (Higashiyama Foot & Kiyomizu)",
                "transit_fatigue_score": "Zero Transit Fatigue (100% pedestrian historic zone)",
                "transit_notes": "Continuous stone-paved pedestrian path from Kiyomizu-dera through Sannenzaka, Ninenzaka to Yasaka Shrine.",
                "slots": {
                    "morning": {
                        "time": "08:30 - 11:30",
                        "title": "Kiyomizu-dera Wooden Stage & Otowa Waterfall",
                        "description": "Stand on the massive 13-meter wooden veranda built without a single nail overlooking maple tree canopy and drink from sacred spring streams.",
                        "estimated_cost": 8.0,
                        "vibe": "Panoramic Historic",
                        "tips": "Choose one stream only at Otowa: health, longevity, or success in studies."
                    },
                    "lunch": {
                        "time": "12:00 - 13:30",
                        "title": "Yudofu (Simmered Tofu) at Junsei Nanzenji",
                        "description": "Delicate silken Kyoto tofu simmered in kombu kelp broth served with ginger sauce inside a 200-year-old registered landscape garden.",
                        "estimated_cost": 38.0,
                        "vibe": "Zen Gastronomy",
                        "tips": "Ask for seating overlooking the koi pond."
                    },
                    "afternoon": {
                        "time": "14:00 - 17:00",
                        "title": "Sannenzaka, Ninenzaka & Kodai-ji Temple",
                        "description": "Stone staircases with heritage wooden merchant storefronts, pottery shops, and Kodai-ji's peaceful weeping cherry tree garden.",
                        "estimated_cost": 10.0,
                        "vibe": "Heritage Walk",
                        "tips": "Pick up handmade Kiyomizu-yaki ceramics and yuzu treats as gifts."
                    },
                    "evening": {
                        "time": "18:30 - 21:00",
                        "title": "Lantern Glow at Yasaka Shrine & Shijo Dori Dining",
                        "description": "Witness hundreds of illuminated paper lanterns at Yasaka Shrine, followed by a cozy dinner of Okonomiyaki pancakes.",
                        "estimated_cost": 28.0,
                        "vibe": "Lantern Enchantment",
                        "tips": "Night photos under Yasaka's central dance stage lanterns are spectacular."
                    }
                },
                "day_cost": 84.0
            },
            {
                "day_number": 5,
                "title": "Great Bronze Buddha & Bowing Sacred Deer of Nara",
                "cluster_zone": "Nara Historic Park Excursion (South Kyoto)",
                "transit_fatigue_score": "Smooth (35-min express Kintetsu train straight into Nara)",
                "transit_notes": "Kintetsu-Kyoto line express to Kintetsu-Nara; entire Nara Park precinct is flat and walkable.",
                "slots": {
                    "morning": {
                        "time": "09:00 - 12:00",
                        "title": "Todai-ji Temple & Daibutsu (Giant Buddha)",
                        "description": "Enter the world's largest wooden building sheltering a colossal 15-meter bronze Buddha, surrounded by hundreds of friendly bowing Shika deer.",
                        "estimated_cost": 10.0,
                        "vibe": "Monumental Spiritual",
                        "tips": "Buy 'shika senbei' deer crackers (200 yen) to interact gently with the deer."
                    },
                    "lunch": {
                        "time": "12:30 - 14:00",
                        "title": "Miwa Somen Noodles & Persimmon-Leaf Sushi at Hiraso",
                        "description": "Historic Nara delicacy of mackerel and salmon wrapped in persimmon leaves paired with ultra-thin wheat noodles.",
                        "estimated_cost": 22.0,
                        "vibe": "Regional Delicacy",
                        "tips": "Unwrap the persimmon leaf before eating; it imparts a subtle fragrance."
                    },
                    "afternoon": {
                        "time": "14:30 - 17:00",
                        "title": "Kasuga Taisha Shrine of 3,000 Lanterns & Naramachi Merchant Quarter",
                        "description": "Mossy woodland path lined with stone lanterns leading to the sacred vermilion shrine, ending with browsing traditional machiya houses.",
                        "estimated_cost": 8.0,
                        "vibe": "Forest Shrine & Crafts",
                        "tips": "Visit Nakatanidou in Naramachi to watch lightning-fast high-speed mochi pounding."
                    },
                    "evening": {
                        "time": "18:00 - 20:30",
                        "title": "Celebratory Farewell Soba & Sake Toast",
                        "description": "Hand-cut buckwheat soba noodles with crispy tempura and local Nara Harushika sake, celebrating an unforgettable journey.",
                        "estimated_cost": 35.0,
                        "vibe": "Farewell Feast",
                        "tips": "Reflect on itinerary memories and pack travel souvenirs."
                    }
                },
                "day_cost": 75.0
            }
        ]
    },
    {
        "id": "amalfi-coast-02",
        "title": "Amalfi Coast & Capri Cliffside Mediterranean Romance",
        "destination": "Amalfi Coast, Italy",
        "duration": 4,
        "start_date": "2026-06-15",
        "end_date": "2026-06-18",
        "budget_tier": "Luxury ($$$/₹₹₹)",
        "party_type": "Couple / Romantic",
        "pace": "Relaxed",
        "currency": "EUR (€)",
        "created_at": "2026-10-26 15:00",
        "estimated_total_cost": 1820.0,
        "vibe_tag": "Romantic & Scenic Escapes",
        "transit_summary": "Optimized marine and coastal transit: Positano Base (Day 1) -> Hydrofoil Capri Island (Day 2) -> Ravello High Gardens & Amalfi (Day 3) -> Sentiero degli Dei & Praiano (Day 4). Eliminates bus gridlock by using private boats.",
        "days": [
            {
                "day_number": 1,
                "title": "Pastel Cascades & Private Gozzo Boat Cruise",
                "cluster_zone": "Positano Coastal & Sea Caves",
                "transit_fatigue_score": "Exceptional (Zero bus transit, private wooden boat)",
                "transit_notes": "Depart directly from Positano pier on private chartered Italian gozzo boat.",
                "slots": {
                    "morning": {
                        "time": "09:30 - 12:30",
                        "title": "Positano Cliffside Exploration & Spiaggia Grande",
                        "description": "Wander through bougainvillea-draped stairways, linen boutiques, and relax on pebble shores.",
                        "estimated_cost": 30.0,
                        "vibe": "Coastal Elegance",
                        "tips": "Wear comfortable flat leather sandals for steep stairs."
                    },
                    "lunch": {
                        "time": "13:00 - 14:30",
                        "title": "Cliffside Seafood Lunch at Chez Black",
                        "description": "Iconic seaside restaurant serving famous heart-shaped lobster pizza and spaghetti with sea urchins.",
                        "estimated_cost": 95.0,
                        "vibe": "Glamorous Seaside",
                        "tips": "Request front-row terrace seating facing the water."
                    },
                    "afternoon": {
                        "time": "15:00 - 18:00",
                        "title": "Private Gozzo Boat to Laurito & Hidden Sea Caves",
                        "description": "Sail past Faraglioni coastal arches, swim in crystal turquoise sea grottos with prosecco on board.",
                        "estimated_cost": 220.0,
                        "vibe": "Pure Romance",
                        "tips": "Towels and snorkel gear provided by boat skipper."
                    },
                    "evening": {
                        "time": "19:30 - 22:30",
                        "title": "Candlelight Dinner at Franco's Bar & La Sponda",
                        "description": "Pre-dinner Bellinis with contemporary art views, followed by dinner illuminated by 400 beeswax candles.",
                        "estimated_cost": 160.0,
                        "vibe": "Michelin Romantic",
                        "tips": "Book La Sponda weeks in advance; candle illumination begins at dusk."
                    }
                },
                "day_cost": 505.0
            },
            {
                "day_number": 2,
                "title": "Capri Island Glamour & Monte Solaro Panorama",
                "cluster_zone": "Capri & Anacapri Island",
                "transit_fatigue_score": "High (Hydrofoil + single chairlift ride, no switchbacks)",
                "transit_notes": "Fast hydrofoil from Positano pier to Marina Grande Capri (25 mins).",
                "slots": {
                    "morning": {
                        "time": "09:00 - 12:00",
                        "title": "Marina Grande to Blue Grotto & Augustus Gardens",
                        "description": "Rowboat entry into the glowing azure sea cave, then walk through terraced gardens overlooking Via Krupp.",
                        "estimated_cost": 45.0,
                        "vibe": "Natural Wonder",
                        "tips": "Blue Grotto entry depends on calm tide; morning light offers purest cobalt hue."
                    },
                    "lunch": {
                        "time": "12:30 - 14:30",
                        "title": "Ristorante Da Paolino Lemon Trees",
                        "description": "Dine beneath a fragrant canopy of thousands of ripe hanging lemons, savoring handmade ravioli capresi.",
                        "estimated_cost": 110.0,
                        "vibe": "Lemon Grove Luxury",
                        "tips": "Do not skip their signature limoncello soufflé dessert."
                    },
                    "afternoon": {
                        "time": "15:00 - 17:30",
                        "title": "Anacapri Single Chairlift to Monte Solaro Peak",
                        "description": "Glide silently above vineyards on single open-air chairlift reaching the highest vantage point of Capri (589m).",
                        "estimated_cost": 18.0,
                        "vibe": "Spectacular 360° Views",
                        "tips": "Incredible photo spot of the Faraglioni limestone sea stacks."
                    },
                    "evening": {
                        "time": "18:30 - 21:30",
                        "title": "Piazzetta Sunset Spritz & Return Hydrofoil",
                        "description": "Sip Aperol Spritz in 'The World's Living Room' for celebrity-watching before smooth sunset sail back to Positano.",
                        "estimated_cost": 65.0,
                        "vibe": "La Dolce Vita",
                        "tips": "Catch the 19:15 return boat to catch sunset from the water."
                    }
                },
                "day_cost": 238.0
            },
            {
                "day_number": 3,
                "title": "Hilltop Gardens of Ravello & Cathedral of Amalfi",
                "cluster_zone": "Ravello & Central Amalfi Basin",
                "transit_fatigue_score": "High (Clustered hilltop first, descending to sea level)",
                "transit_notes": "Private Mercedes van to Ravello hilltop; descend leisurely into Amalfi town.",
                "slots": {
                    "morning": {
                        "time": "09:30 - 12:30",
                        "title": "Villa Rufolo & Infinity Terrace of Villa Cimbrone",
                        "description": "Stroll through Wagner's inspiring Moorish gardens and stand on the marble bust-lined 'Belvedere of Infinity'.",
                        "estimated_cost": 22.0,
                        "vibe": "Aristocratic Heritage",
                        "tips": "Widely acclaimed as the finest sea viewpoint on earth."
                    },
                    "lunch": {
                        "time": "13:00 - 14:30",
                        "title": "Babel Wine Bar Deli & Art",
                        "description": "Artisan charcuterie, burrata with figs, and organic Campania Greco di Tufo white wine in Ravello piazza.",
                        "estimated_cost": 50.0,
                        "vibe": "Charming Bistro",
                        "tips": "Owner pairs exceptional local boutique wines not found in commercial markets."
                    },
                    "afternoon": {
                        "time": "15:00 - 17:30",
                        "title": "Duomo di Amalfi (St. Andrew's Cathedral) & Paper Mill Museum",
                        "description": "Ascend the 62 steps of the 9th-century striped Arab-Norman cathedral and see historic Amalfi handmade cotton paper.",
                        "estimated_cost": 12.0,
                        "vibe": "Maritime Republic History",
                        "tips": "Cloister of Paradise inside the cathedral offers breathtaking quiet."
                    },
                    "evening": {
                        "time": "18:30 - 21:30",
                        "title": "Dinner at Marina Grande Restaurant & Gelato Walk",
                        "description": "Fresh catch of the day salted sea bass with local lemons, ending with artisanal dark chocolate lemon gelato.",
                        "estimated_cost": 120.0,
                        "vibe": "Waterfront Gourmet",
                        "tips": "Try local Delizia al Limone pastry for dessert."
                    }
                },
                "day_cost": 204.0
            },
            {
                "day_number": 4,
                "title": "Path of the Gods & Sunset Aperitivo in Praiano",
                "cluster_zone": "Upper Coastal Ridge & Praiano",
                "transit_fatigue_score": "Moderate Active (Scenic ridge walk followed by relaxed coastal lounge)",
                "transit_notes": "Start at Bomerano ridge trail descending gently towards Nocelle.",
                "slots": {
                    "morning": {
                        "time": "08:30 - 12:30",
                        "title": "Sentiero degli Dei (Path of the Gods) Guided Hike",
                        "description": "Spectacular 7km cliff trail suspended between sky and Mediterranean sea with breathtaking Capri panoramas.",
                        "estimated_cost": 40.0,
                        "vibe": "Adventure & Nature",
                        "tips": "Bring sturdy trail shoes, sun hat, and 1.5L water."
                    },
                    "lunch": {
                        "time": "13:00 - 14:30",
                        "title": "Rifugio dei Mele Farmhouse Lunch in Nocelle",
                        "description": "Rustic cliffside terrace serving fresh paccheri pasta with slow-cooked wild boar ragu and fresh ricotta.",
                        "estimated_cost": 55.0,
                        "vibe": "Farm-to-Table Panoramas",
                        "tips": "Reward yourself after the hike with freshly squeezed organic pomegranate juice."
                    },
                    "afternoon": {
                        "time": "15:30 - 18:00",
                        "title": "Praiano Artisan Ceramic Studio & Lemon Grove Tour",
                        "description": "Meet master potters hand-painting vibrant majolica ceramic plates, followed by tasting cold limoncello.",
                        "estimated_cost": 25.0,
                        "vibe": "Artisanal Craft",
                        "tips": "Studios provide worldwide bubble-wrapped shipping for ceramics."
                    },
                    "evening": {
                        "time": "19:00 - 22:00",
                        "title": "Sunset Cocktails at Café Margherita & Farewell Seafood Feast",
                        "description": "Praiano enjoys the latest and most fiery sunset on the coast; conclude with grilled Mediterranean prawns and Amalfi lemon cake.",
                        "estimated_cost": 110.0,
                        "vibe": "Golden Sunset Celebration",
                        "tips": "Toast to an extraordinary Italian coastal romance."
                    }
                },
                "day_cost": 230.0
            }
        ]
    },
    {
        "id": "rajasthan-royal-03",
        "title": "Royal Rajasthan: Jaipur Pink City & Udaipur Lake Palaces",
        "destination": "Jaipur & Udaipur, Rajasthan, India",
        "duration": 5,
        "start_date": "2026-12-01",
        "end_date": "2026-12-05",
        "budget_tier": "Moderate ($$/₹₹)",
        "party_type": "Family (with Children/Seniors)",
        "pace": "Moderate",
        "currency": "INR (₹)",
        "created_at": "2026-10-26 15:30",
        "estimated_total_cost": 48500.0,
        "vibe_tag": "Cultural & Historic Heritage",
        "transit_summary": "Zone-based itinerary: Walled Old Pink City (Day 1) -> Amer Fort Ridge (Day 2) -> Royal Bazaars & Palaces (Day 3) -> Lake Pichola Udaipur (Day 4) -> City Palace & Sajjangarh (Day 5). Avoids inter-city zigzagging.",
        "days": [
            {
                "day_number": 1,
                "title": "Walled Pink City, Honeycomb Façades & Royal Astronomy",
                "cluster_zone": "Jaipur Walled City Heritage Zone",
                "transit_fatigue_score": "High Optimization (All sights within 1.5 km walking radius)",
                "transit_notes": "Drop off at Badi Chaupar; explore Hawa Mahal, City Palace, and Jantar Mantar continuously.",
                "slots": {
                    "morning": {
                        "time": "08:30 - 12:00",
                        "title": "Hawa Mahal (Palace of Winds) & City Palace Jaipur",
                        "description": "Admire the 953 honeycomb windows designed for royal ladies to observe street processions, then tour the Maharaja's active royal residence and courtyards.",
                        "estimated_cost": 1600.0,
                        "vibe": "Royal Architecture",
                        "tips": "Photograph Hawa Mahal façade from Wind View Café across the street in early morning light."
                    },
                    "lunch": {
                        "time": "12:30 - 14:00",
                        "title": "Traditional Rajasthani Thali at LMB (Laxmi Misthan Bhandar)",
                        "description": "Famous 1954 heritage restaurant in Johari Bazaar serving royal Dal Baati Churma, Gatte ki Sabzi, and hot Ghewar.",
                        "estimated_cost": 1800.0,
                        "vibe": "Authentic Cuisine",
                        "tips": "Save room for Malpua and Mawa Kachori sweet delicacies."
                    },
                    "afternoon": {
                        "time": "14:30 - 17:00",
                        "title": "Jantar Mantar UNESCO Astronomical Observatory",
                        "description": "Discover stone sundials and world's largest stone equinoctial sundial built by Maharaja Sawai Jai Singh II in 1734.",
                        "estimated_cost": 800.0,
                        "vibe": "Scientific Heritage",
                        "tips": "Hire an official audio guide or licensed astronomy guide to understand the instruments."
                    },
                    "evening": {
                        "time": "18:00 - 21:30",
                        "title": "Chokhi Dhani Ethnic Cultural Village",
                        "description": "Immersive village fair with Rajasthani folk dancers (Kalbeliya), puppet shows, camel rides, and traditional sit-down banquet on floor mats.",
                        "estimated_cost": 3200.0,
                        "vibe": "Cultural Festival",
                        "tips": "Wonderful for families with kids; arrive right at 6 PM opening."
                    }
                },
                "day_cost": 7400.0
            },
            {
                "day_number": 2,
                "title": "Amber Ramparts, Mirrored Halls & Sunset Ridge",
                "cluster_zone": "Amer Hilltop Ridge (North Jaipur)",
                "transit_fatigue_score": "Clustered (Amer, Panna Meena Kund & Nahargarh on same ridge)",
                "transit_notes": "Single cab booked for the entire northern hill circuit without backtracking into city center.",
                "slots": {
                    "morning": {
                        "time": "08:30 - 12:30",
                        "title": "Amer Fort & Sheesh Mahal (Hall of Mirrors)",
                        "description": "Massive sandstone fortress towering over Maota Lake, famous for its dazzling mosaic mirror palace that glows with a single candle.",
                        "estimated_cost": 2200.0,
                        "vibe": "Epic Fortresses",
                        "tips": "Wear comfortable walking shoes; the ramparts have cobblestones and gentle slopes."
                    },
                    "lunch": {
                        "time": "13:00 - 14:30",
                        "title": "1135 AD Fine Dining inside Amer Fort Ramparts",
                        "description": "Opulent silver service dining beneath gold leaf ceilings and crystal chandeliers serving regal Mughlai recipes.",
                        "estimated_cost": 4500.0,
                        "vibe": "Regal Luxury Dining",
                        "tips": "Order the Royal Lal Maas (tender spiced mutton curry) or Kesari Paneer."
                    },
                    "afternoon": {
                        "time": "15:00 - 17:00",
                        "title": "Panna Meena ka Kund Stepwell & Anokhi Museum of Hand Printing",
                        "description": "Mesmerizing geometric 16th-century stepped water reservoir and live demonstration of heritage wooden block printing on fine cotton.",
                        "estimated_cost": 600.0,
                        "vibe": "Craft & Architecture",
                        "tips": "Try your own hand at wooden block printing your personal bandana."
                    },
                    "evening": {
                        "time": "17:30 - 21:00",
                        "title": "Sunset View from Nahargarh Fort & Padao Open Air Lounge",
                        "description": "Watch the sun dip below the Aravalli hills with 360-degree twilight views of the entire Jaipur city glittering below.",
                        "estimated_cost": 2400.0,
                        "vibe": "Panoramic Twilight",
                        "tips": "Take the winding forest road up before 5:00 PM to secure prime cliffside edge tables."
                    }
                },
                "day_cost": 9700.0
            },
            {
                "day_number": 3,
                "title": "Jewel Bazaars, Rainbow Arches & Albert Hall Night Glow",
                "cluster_zone": "South & Central Jaipur Craft Hubs",
                "transit_fatigue_score": "Zero Transit Strain (Gentle pacing with afternoon tea break)",
                "transit_notes": "Auto-rickshaws for short hops between bazaars and gardens.",
                "slots": {
                    "morning": {
                        "time": "09:30 - 12:00",
                        "title": "Patrika Gate & Jawahar Circle Garden",
                        "description": "Walk beneath nine intricately hand-painted arches illustrating Rajasthani royalty, culture, and architecture.",
                        "estimated_cost": 0.0,
                        "vibe": "Vibrant Photography",
                        "tips": "Morning light highlights the vivid pastels inside the corridor."
                    },
                    "lunch": {
                        "time": "12:30 - 14:00",
                        "title": "Kafila Heritage Restaurant",
                        "description": "North Indian and Afghani culinary delights in an Afghan tent-inspired royal setting.",
                        "estimated_cost": 2200.0,
                        "vibe": "Gourmet Midday",
                        "tips": "Try the smoked dahi ke kabab and garlic naan."
                    },
                    "afternoon": {
                        "time": "14:30 - 17:30",
                        "title": "Johari Bazaar & Bapu Bazaar Artisan Walk",
                        "description": "Bargain for genuine gemstone jewelry, Jaipuri blue pottery, hand-stitched quilts (Razai), and mojari leather shoes.",
                        "estimated_cost": 2000.0,
                        "vibe": "Bustling Bazaars",
                        "tips": "Polite bargaining is customary; check for government hallmarking on silver."
                    },
                    "evening": {
                        "time": "18:00 - 20:30",
                        "title": "Albert Hall State Central Museum Illuminated by Night",
                        "description": "Indo-Saracenic architectural masterpiece glowing with multi-colored floodlights, surrounded by pigeons and evening performers.",
                        "estimated_cost": 900.0,
                        "vibe": "Night Illumination",
                        "tips": "Night ticket grants entry to the Egyptian mummy and coin galleries."
                    }
                },
                "day_cost": 5100.0
            },
            {
                "day_number": 4,
                "title": "Venice of the East: Lake Pichola & Sunset Boat Cruise",
                "cluster_zone": "Udaipur Pichola Waterfront",
                "transit_fatigue_score": "Smooth Arrival & Lake Relaxation",
                "transit_notes": "Morning scenic transfer to Udaipur; afternoon completely based around Lake Pichola docks.",
                "slots": {
                    "morning": {
                        "time": "09:00 - 12:30",
                        "title": "Arrival in Udaipur & Check-in along Lake Pichola",
                        "description": "Scenic arrival in the city of lakes, checking into a heritage haveli hotel overlooking tranquil waters.",
                        "estimated_cost": 1500.0,
                        "vibe": "Scenic Tranquility",
                        "tips": "Keep camera ready as you drive past the ancient city gates."
                    },
                    "lunch": {
                        "time": "13:00 - 14:30",
                        "title": "Lake View Lunch at Jheel's Ginger Coffee Bar",
                        "description": "Wood-fired pizzas, ginger tea, and cold frappes right on the edge of the lake watching boats glide by.",
                        "estimated_cost": 1600.0,
                        "vibe": "Lakeside Casual",
                        "tips": "Top floor terrace has the most intimate water view."
                    },
                    "afternoon": {
                        "time": "15:00 - 17:30",
                        "title": "Lake Pichola Royal Boat Cruise to Jag Mandir Island",
                        "description": "Private motorized boat sailing past the floating white marble Lake Palace to the 17th-century island palace garden.",
                        "estimated_cost": 2800.0,
                        "vibe": "Island Romance",
                        "tips": "Jag Mandir's stone marble elephants at the dock make an unforgettable photo."
                    },
                    "evening": {
                        "time": "18:30 - 21:30",
                        "title": "Bagore Ki Haveli Dharohar Folk Dance & Lakeside Dinner at Ambrai",
                        "description": "Spectacular 1-hour live performance with ladies balancing 11 brass pots on their heads, followed by candlelit dining facing the illuminated City Palace.",
                        "estimated_cost": 4200.0,
                        "vibe": "Living Tradition",
                        "tips": "Pre-book Ambrai table right next to the water railing at least 48 hours prior."
                    }
                },
                "day_cost": 10100.0
            },
            {
                "day_number": 5,
                "title": "Grand City Palace, Maiden Fountains & Sunset Monsoon Palace",
                "cluster_zone": "Udaipur Heritage Core & Sajjangarh Ridge",
                "transit_fatigue_score": "High (Palace exploration followed by scenic hilltop ascent)",
                "transit_notes": "Old city walking path to City Palace, followed by eco-van to Sajjangarh hilltop.",
                "slots": {
                    "morning": {
                        "time": "09:00 - 12:30",
                        "title": "Udaipur City Palace Complex & Crystal Gallery",
                        "description": "Rajasthan's largest royal palace complex featuring peacock courtyards, mirror chambers, and silver carriage galleries.",
                        "estimated_cost": 2500.0,
                        "vibe": "Architectural Jewel",
                        "tips": "Visit Mor Chowk (Peacock Courtyard) to see 5,000 glass mosaic tiles."
                    },
                    "lunch": {
                        "time": "13:00 - 14:30",
                        "title": "Tribute Restaurant overlooking Fateh Sagar Lake",
                        "description": "Dedicated to Chetak, the legendary loyal horse of Maharana Pratap; serves delicious Rajasthani and tandoori grills.",
                        "estimated_cost": 2600.0,
                        "vibe": "Lakeview Dining",
                        "tips": "Try the Mutton Dhungar and Ker Sangri berry delicacies."
                    },
                    "afternoon": {
                        "time": "15:00 - 17:00",
                        "title": "Saheliyon-ki-Bari (Garden of the Royal Maids)",
                        "description": "Lush historic gardens engineered with natural gravity-fed marble fountains, lotus pools, and sculpted stone elephants.",
                        "estimated_cost": 400.0,
                        "vibe": "Botanical Heritage",
                        "tips": "Listen to the rain sound illusion created by the overhead fountain domes."
                    },
                    "evening": {
                        "time": "17:30 - 21:00",
                        "title": "Monsoon Palace (Sajjangarh) Hilltop Sunset & Farewell Feast",
                        "description": "High atop the Bansdara peak of the Aravallis, enjoy golden sunset views over the entire lake valley followed by a royal farewell dinner.",
                        "estimated_cost": 3800.0,
                        "vibe": "Crowning Panorama",
                        "tips": "Wildlife sanctuary electric jeeps take you up to the palace peak."
                    }
                },
                "day_cost": 9300.0
            }
        ]
    }
]
