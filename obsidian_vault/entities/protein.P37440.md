---
entity_id: "protein.P37440"
entity_type: "protein"
name: "ucpA"
source_database: "UniProt"
source_id: "P37440"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ucpA yfeF b2426 JW5394"
---

# ucpA

`protein.P37440`

## Static

- Type: `protein`
- Source: `UniProt:P37440`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Oxidoreductase UcpA (EC 1.-.-.-) Based on sequence similarity, UcpA was predicted to be an acetoin dehydrogenase (diacetyl reductase) . Recent data show that UcpA is in fact able to reduce diacetyl to acetoin . A range of potential substrates, including diacetyl and acetoin, was previously tested in cell extracts of a strain overexpressing UcpA, and no increased activity compared to control extracts was found . Crp, FruR and IHF are involved in the regulation of ucpA . Expression of ucpA is upregulated by furfural, and overexpression of ucpA increases furan tolerance in an engineered E. coli strain and in the wild-type E. coli W strain . A knockout mutation of ucpA negatively affected conjugation efficiency after 24-48 hrs; UcpA's putative role in fermentation may help restore intracellular pH thus improving conjugation efficiency . UcpA: "upstream of cysP"

## Biological Role

Catalyzes RXN-11032 (reaction.ecocyc.RXN-11032).

## Annotation

Oxidoreductase UcpA (EC 1.-.-.-)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11032|reaction.ecocyc.RXN-11032]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2426|gene.b2426]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37440`
- `KEGG:ecj:JW5394;eco:b2426;ecoc:C3026_13480;`
- `GeneID:75204304;946898;`
- `GO:GO:0052588`
- `EC:1.-.-.-`

## Notes

Oxidoreductase UcpA (EC 1.-.-.-)
