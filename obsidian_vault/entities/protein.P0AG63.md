---
entity_id: "protein.P0AG63"
entity_type: "protein"
name: "rpsQ"
source_database: "UniProt"
source_id: "P0AG63"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpsQ neaA b3311 JW3273"
---

# rpsQ

`protein.P0AG63`

## Static

- Type: `protein`
- Source: `UniProt:P0AG63`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: One of the primary rRNA binding proteins, it binds specifically to the 5'-end of 16S ribosomal RNA (PubMed:4598121). Also plays a role in translational accuracy; neamine-resistant ribosomes show reduced neamine-induced misreading in vitro (PubMed:765484, PubMed:781296). {ECO:0000269|PubMed:4598121, ECO:0000269|PubMed:765484, ECO:0000269|PubMed:781296}. The S17 protein is a component of the 30S subunit of the ribosome . S17 stabilizes the tertiary structure of the entire 5' domain of 16S rRNA, including non-native folding intermediates . An S17-stabilized non-native folding intermediate appears to be the preferred substrate for EG12044-MONOMER . S17, S4 and S20 together pre-organize the binding site for S16 . Molecular dynamics simulations indicate that binding of S16 rescues the structure of the helix 17 internal loop that is disrupted by previous binding of S17 . The 30S subunit assembly defect due to depleting S17 was analyzed in vivo . S17 binds directly to the 5' domain of 16S rRNA . Specific contact sites have been identified . S17 can also be crosslinked to tRNA in the A site and to the release factor RF-2 . S17 is encoded as part of the S10 operon . The initiating methionine of S17 is cleaved . A conditionally lethal point mutation in rpsQ leads to impaired assembly of the 30S ribosomal subunit...

## Biological Role

Component of 30S ribosomal subunit (complex.ecocyc.CPLX0-3953).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: One of the primary rRNA binding proteins, it binds specifically to the 5'-end of 16S ribosomal RNA (PubMed:4598121). Also plays a role in translational accuracy; neamine-resistant ribosomes show reduced neamine-induced misreading in vitro (PubMed:765484, PubMed:781296). {ECO:0000269|PubMed:4598121, ECO:0000269|PubMed:765484, ECO:0000269|PubMed:781296}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3953|complex.ecocyc.CPLX0-3953]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b3311|gene.b3311]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG63`
- `KEGG:ecj:JW3273;eco:b3311;ecoc:C3026_17995;`
- `GeneID:86862291;93778676;947808;`
- `GO:GO:0000028; GO:0002181; GO:0003735; GO:0005737; GO:0008270; GO:0019843; GO:0022627; GO:0046677; GO:0070181`

## Notes

Small ribosomal subunit protein uS17 (30S ribosomal protein S17)
