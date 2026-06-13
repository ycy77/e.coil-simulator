---
entity_id: "protein.P0AGD7"
entity_type: "protein"
name: "ffh"
source_database: "UniProt"
source_id: "P0AGD7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm. Note=The SRP-RNC complex is targeted to the cytoplasmic membrane."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ffh b2610 JW5414"
---

# ffh

`protein.P0AGD7`

## Static

- Type: `protein`
- Source: `UniProt:P0AGD7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm. Note=The SRP-RNC complex is targeted to the cytoplasmic membrane.

## Enriched Summary

FUNCTION: Involved in targeting and insertion of nascent membrane proteins into the cytoplasmic membrane. Binds to the hydrophobic signal sequence of the ribosome-nascent chain (RNC) as it emerges from the ribosomes. The SRP-RNC complex is then targeted to the cytoplasmic membrane where it interacts with the SRP receptor FtsY. Interaction with FtsY leads to the transfer of the RNC complex to the Sec translocase for insertion into the membrane, the hydrolysis of GTP by both Ffh and FtsY, and the dissociation of the SRP-FtsY complex into the individual components. {ECO:0000255|HAMAP-Rule:MF_00306, ECO:0000269|PubMed:11735405, ECO:0000269|PubMed:11741850, ECO:0000269|PubMed:1279430, ECO:0000269|PubMed:1331806, ECO:0000269|PubMed:15140892, ECO:0000269|PubMed:2171778, ECO:0000269|PubMed:9305630}. The structure of Ffh has been analyzed alone and in a complex with the 4.5 S RNA . Ffh contains two domains: a methionine rich M domain and an NG domain containing an N-terminal 4 helix bundle plus a G region which contains the signature motifs of the GTPase family. 4.5S RNA folds into a single hairpin structure containing an apical GGAA tetraloop that caps one end plus five symmetric or asymmetic internal loops (reviews: . The two ends of the 4.5S RNA hairpin have distinct functions in the targeting cycle . Oxidized Ffh is unable to bind 4...

## Biological Role

Catalyzes GTP phosphohydrolase (reaction.R00335). Component of Signal Recognition Particle (complex.ecocyc.SRP-CPLX).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Involved in targeting and insertion of nascent membrane proteins into the cytoplasmic membrane. Binds to the hydrophobic signal sequence of the ribosome-nascent chain (RNC) as it emerges from the ribosomes. The SRP-RNC complex is then targeted to the cytoplasmic membrane where it interacts with the SRP receptor FtsY. Interaction with FtsY leads to the transfer of the RNC complex to the Sec translocase for insertion into the membrane, the hydrolysis of GTP by both Ffh and FtsY, and the dissociation of the SRP-FtsY complex into the individual components. {ECO:0000255|HAMAP-Rule:MF_00306, ECO:0000269|PubMed:11735405, ECO:0000269|PubMed:11741850, ECO:0000269|PubMed:1279430, ECO:0000269|PubMed:1331806, ECO:0000269|PubMed:15140892, ECO:0000269|PubMed:2171778, ECO:0000269|PubMed:9305630}.

## Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00335|reaction.R00335]] `KEGG` `database` - via EC:3.6.5.4
- `is_component_of` --> [[complex.ecocyc.SRP-CPLX|complex.ecocyc.SRP-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b2610|gene.b2610]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGD7`
- `KEGG:ecj:JW5414;eco:b2610;ecoc:C3026_14450;`
- `GeneID:86860732;93774460;947102;`
- `GO:GO:0003924; GO:0005525; GO:0005829; GO:0006612; GO:0006614; GO:0008312; GO:0048500; GO:1990904`
- `EC:3.6.5.4`

## Notes

Signal recognition particle protein (EC 3.6.5.4) (Fifty-four homolog) (Ffh) (p48)
