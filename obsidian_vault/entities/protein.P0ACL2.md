---
entity_id: "protein.P0ACL2"
entity_type: "protein"
name: "exuR"
source_database: "UniProt"
source_id: "P0ACL2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "exuR b3094 JW3065"
---

# exuR

`protein.P0ACL2`

## Static

- Type: `protein`
- Source: `UniProt:P0ACL2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Repressor for the exu regulon that encode genes involved in hexuronate utilization. It regulates the ExuT, UxaCA and UxuRAB operons. Binds D-tagaturonate and D-fructuronate as inducers. The "Exuronate" repressor ExuR, is a DNA-binding transcription factor that negatively regulates its own synthesis and represses transcription of the operons involved in transport and catabolism of galacturonate and glucuronate . ExuR is similar to UxuR (49% of identity), and apparently both act together and are capable of cross-talk to regulate expression of the uxu operon . For this reason, there is the possibility that these regulators bind the same sites with different affinities. ExuR binds to the exuR regulatory region in the presence of glucuronate and inhibits the expression of exuR. This repression is partially affected by the presence of UxuR, since UxuR is capable of binding to the same regulatory region as ExuR . ExuR has been shown to act as a repressor that binds to a putative inverted repeat sequence . The promoter activity of exuR was increased during cell growth in the presence of glucuronate compared to growth with glucose as a main carbon source. Higher activities were found also in a uxuR mutant strain grown in the presence of glucose as a carbon source. However, this response was not observed in an exuR mutant strain...

## Biological Role

Component of ExuR-α-D-galacturonate, α-D-glucuronate-DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-8210), ExuR-α-D-glucuronate (complex.ecocyc.CPLX0-8246).

## Annotation

FUNCTION: Repressor for the exu regulon that encode genes involved in hexuronate utilization. It regulates the ExuT, UxaCA and UxuRAB operons. Binds D-tagaturonate and D-fructuronate as inducers.

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8210|complex.ecocyc.CPLX0-8210]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-8246|complex.ecocyc.CPLX0-8246]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b3094|gene.b3094]] `RegulonDB` `S` - regulator=ExuR; target=exuR; function=-
- `represses` --> [[gene.b4357|gene.b4357]] `RegulonDB` `S` - regulator=ExuR; target=lgoR; function=-
- `represses` --> [[gene.b4358|gene.b4358]] `RegulonDB` `S` - regulator=ExuR; target=lgoD; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3094|gene.b3094]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACL2`
- `KEGG:ecj:JW3065;eco:b3094;ecoc:C3026_16895;`
- `GeneID:93778889;947602;`
- `GO:GO:0000987; GO:0003700; GO:0006355; GO:0045892`

## Notes

Exu regulon transcriptional regulator
