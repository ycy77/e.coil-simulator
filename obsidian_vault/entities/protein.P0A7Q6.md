---
entity_id: "protein.P0A7Q6"
entity_type: "protein"
name: "rpmJ"
source_database: "UniProt"
source_id: "P0A7Q6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpmJ b3299 JW3261"
---

# rpmJ

`protein.P0A7Q6`

## Static

- Type: `protein`
- Source: `UniProt:P0A7Q6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: One of the last ribosomal proteins to be assembled in the 50S subunit, it contacts a number of helices in the 23S rRNA, acting as molecular glue (PubMed:33639093). The simultaneous presence of uL16 and bL36 probably triggers ObgE's GTPase activity and eventual dissociation from the mature 50S ribosomal subunit (PubMed:33639093). {ECO:0000269|PubMed:33639093}. The L36 protein is a component of the 50S subunit of the ribosome . L36 is highly conserved in bacteria, mitochondria and chloroplasts, but not present in archaea and eukarya . Ribosomes lacking L36 are correctly assembled. However, chemical protection experiments suggest that rRNA tertiary interactions are disrupted in ribosomes lacking L36, thus arguing that L36 plays a significant role in organizing 23S rRNA structure . 2'-O-methylation of U2552 by EG11507-MONOMER promotes association between helices 92 and 71 of 23S rRNA; together with incorporation of L36, it promotes late steps of 50S ribosomal subunit assembly . Profiles of ribosomes isolated from a ΔrpmJ mutant show a minor peak at 40S that lacks the late assembly proteins L16 and L35 . Ribosomes isolated from a ΔEG11507 rlmE strain lack L16, L35 and L36 . L36 has been shown to crosslink to 23S rRNA . Deletion of rpmJ causes a temperature-sensitive growth defect and increased sensitivity to hydroxyurea...

## Biological Role

Component of 50S ribosomal subunit (complex.ecocyc.CPLX0-3962).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: One of the last ribosomal proteins to be assembled in the 50S subunit, it contacts a number of helices in the 23S rRNA, acting as molecular glue (PubMed:33639093). The simultaneous presence of uL16 and bL36 probably triggers ObgE's GTPase activity and eventual dissociation from the mature 50S ribosomal subunit (PubMed:33639093). {ECO:0000269|PubMed:33639093}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3962|complex.ecocyc.CPLX0-3962]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b3299|gene.b3299]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7Q6`
- `KEGG:ecj:JW3261;eco:b3299;`
- `GeneID:947805;99707783;99810664;`
- `GO:GO:0002181; GO:0003735; GO:0005737; GO:0006412; GO:0019843; GO:0022625`

## Notes

Large ribosomal subunit protein bL36A (50S ribosomal protein L36) (Ribosomal protein B)
