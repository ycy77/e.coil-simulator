---
entity_id: "protein.P0AC16"
entity_type: "protein"
name: "folB"
source_database: "UniProt"
source_id: "P0AC16"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "folB ygiG b3058 JW3030"
---

# folB

`protein.P0AC16`

## Static

- Type: `protein`
- Source: `UniProt:P0AC16`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of 7,8-dihydroneopterin to 6-hydroxymethyl-7,8-dihydropterin. Can use L-threo-dihydroneopterin and D-erythro-dihydroneopterin as substrates for the formation of 6-hydroxymethyldihydropterin, but it can also catalyze the epimerization of carbon 2' of dihydroneopterin to dihydromonapterin at appreciable velocity. {ECO:0000269|PubMed:9651328}. Dihydroneopterin aldolase (FolB) is an enzyme in the folate biosynthesis pathway, an important antibacterial drug target. The reaction mechanism has been investigated. The conserved Y53 residue is important for the aldolase reaction . Site-directed mutagenesis of conserved active site residues suggested that E22 is important for substrate binding, but not catalysis, and that E21 and K98 are important for both substrate binding and catalysis . Unlike other aldolase-catalyzed reactions, the dihydroneopterin aldolase reaction was initially found to be irreversible . However, with an enzyme preparation of higher activity and a higher glycolaldehyde concentration, the reaction catalyzed by the Staphylococcus aureus enzyme is readily reversible . A crystal structure of FolB in complex with neopterin has been solved at 1.07Å resolution, and a structural model of the enzyme with the 7,8-dihydroneopterin substrate has been constructed. Structural differences between the E. coli and S...

## Biological Role

Component of dihydroneopterin aldolase (complex.ecocyc.CPLX0-3936).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of 7,8-dihydroneopterin to 6-hydroxymethyl-7,8-dihydropterin. Can use L-threo-dihydroneopterin and D-erythro-dihydroneopterin as substrates for the formation of 6-hydroxymethyldihydropterin, but it can also catalyze the epimerization of carbon 2' of dihydroneopterin to dihydromonapterin at appreciable velocity. {ECO:0000269|PubMed:9651328}.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3936|complex.ecocyc.CPLX0-3936]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## Incoming Edges (1)

- `encodes` <-- [[gene.b3058|gene.b3058]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC16`
- `KEGG:ecj:JW3030;eco:b3058;ecoc:C3026_16710;`
- `GeneID:75173180;947544;`
- `GO:GO:0004150; GO:0005737; GO:0016853; GO:0042802; GO:0046654; GO:0046656`
- `EC:4.1.2.25; 5.1.99.8`

## Notes

Dihydroneopterin aldolase (DHNA) (EC 4.1.2.25) (7,8-dihydroneopterin 2'-epimerase) (7,8-dihydroneopterin aldolase) (7,8-dihydroneopterin epimerase) (EC 5.1.99.8) (Dihydroneopterin epimerase)
