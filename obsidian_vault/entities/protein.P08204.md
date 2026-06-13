---
entity_id: "protein.P08204"
entity_type: "protein"
name: "araB"
source_database: "UniProt"
source_id: "P08204"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "araB b0063 JW0062"
---

# araB

`protein.P08204`

## Static

- Type: `protein`
- Source: `UniProt:P08204`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Ribulokinase (EC 2.7.1.16) Ribulokinase catalyzes the phosphorylation of L-ribulose to L-ribulose-5-phosphate, the second step in the L-arabinose degradation pathway. The araBAD operon and its gene products were first studied in E. coli B/r . The E. coli B ribulokinase has been purified and crystallized , and its subunit structure was determined . The enzyme uses four 2-ketopentoses (L- and D-ribulose, L- and D-xylulose) with similar catalytic activity. In addition, L-arabitol and ribitol can serve as substrates . In the absence of sugar substrates, the enzyme exhibits a low ATPase activity . The sequence of the E. coli B enzyme is 98% identical to the E. coli K-12 enzyme. Transcription of the araBAD operon is induced in the presence of L-arabinose by the transcription factor AraC . araBAD expression can also induced by L-lyxose . araB mutants can not utilize L-arabinose for growth .

## Biological Role

Catalyzes ATP:D-ribulose 5-phosphotransferase (reaction.R01526). Component of ribulokinase (complex.ecocyc.RIBULOKIN-CPLX).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

Ribulokinase (EC 2.7.1.16)

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01526|reaction.R01526]] `KEGG` `database` - via EC:2.7.1.16
- `is_component_of` --> [[complex.ecocyc.RIBULOKIN-CPLX|complex.ecocyc.RIBULOKIN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0063|gene.b0063]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08204`
- `KEGG:ecj:JW0062;eco:b0063;`
- `GeneID:946017;`
- `GO:GO:0005524; GO:0005737; GO:0008741; GO:0016052; GO:0016773; GO:0019150; GO:0019321; GO:0019568; GO:0019569; GO:0019572`
- `EC:2.7.1.16`

## Notes

Ribulokinase (EC 2.7.1.16)
