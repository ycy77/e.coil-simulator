---
entity_id: "protein.P10903"
entity_type: "protein"
name: "narK"
source_database: "UniProt"
source_id: "P10903"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:23665960, ECO:0000269|PubMed:25959928}; Multi-pass membrane protein {ECO:0000269|PubMed:23665960, ECO:0000269|PubMed:25959928}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "narK b1223 JW1214"
---

# narK

`protein.P10903`

## Static

- Type: `protein`
- Source: `UniProt:P10903`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:23665960, ECO:0000269|PubMed:25959928}; Multi-pass membrane protein {ECO:0000269|PubMed:23665960, ECO:0000269|PubMed:25959928}.

## Enriched Summary

FUNCTION: Catalyzes nitrate uptake, nitrite uptake and nitrite export across the cytoplasmic membrane (PubMed:11967075, PubMed:15667293, PubMed:16804183, PubMed:23665960, PubMed:25959928, PubMed:2668029). Functions as a nitrate/nitrite exchanger, and protons are unlikely to be co-transported (PubMed:15667293, PubMed:23665960, PubMed:25959928, PubMed:2668029). {ECO:0000269|PubMed:11967075, ECO:0000269|PubMed:15667293, ECO:0000269|PubMed:16804183, ECO:0000269|PubMed:23665960, ECO:0000269|PubMed:25959928, ECO:0000269|PubMed:2668029}. NarK is a nitrate/nitrite transporter with a physiological role in nitrate-dependent respiration. NarK mediates the uptake of nitrate and the extrusion of nitrite - the exact mechanism of transport has been debated but structural constraints suggest that NarK functions as a nitrate:nitrite exchanger . Purified NarK, reconstituted in liposomes functions as a nitrate:nitrite antiporter . The location of nitrate and nitrite ions in crystal structures of NarK suggest that the two ions bind to the same site competitively (see also ). Early studies characterizing narK mutant alleles in E. coli K-12 include and . Physiological studies of narK deletion mutants implicated the protein in nitrate and nitrite transport and proposed that NarK functions as a nitrate:nitrite antiporter (see also )...

## Biological Role

Catalyzes nitrate:nitrite antiport (reaction.ecocyc.TRANS-RXN0-239). Transports Nitrite (molecule.C00088), Nitrate (molecule.C00244).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes nitrate uptake, nitrite uptake and nitrite export across the cytoplasmic membrane (PubMed:11967075, PubMed:15667293, PubMed:16804183, PubMed:23665960, PubMed:25959928, PubMed:2668029). Functions as a nitrate/nitrite exchanger, and protons are unlikely to be co-transported (PubMed:15667293, PubMed:23665960, PubMed:25959928, PubMed:2668029). {ECO:0000269|PubMed:11967075, ECO:0000269|PubMed:15667293, ECO:0000269|PubMed:16804183, ECO:0000269|PubMed:23665960, ECO:0000269|PubMed:25959928, ECO:0000269|PubMed:2668029}.

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-239|reaction.ecocyc.TRANS-RXN0-239]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00088|molecule.C00088]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00244|molecule.C00244]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1223|gene.b1223]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P10903`
- `KEGG:ecj:JW1214;eco:b1223;ecoc:C3026_07195;`
- `GeneID:93775291;945783;`
- `GO:GO:0005452; GO:0005886; GO:0015112; GO:0015113; GO:0015706; GO:0015707; GO:0042128; GO:0043602`

## Notes

Nitrate/nitrite antiporter NarK (Nitrate/nitrite exchanger) (Nitrite extrusion protein 1) (Nitrite facilitator 1)
