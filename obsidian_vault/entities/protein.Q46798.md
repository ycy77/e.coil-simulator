---
entity_id: "protein.Q46798"
entity_type: "protein"
name: "ygeR"
source_database: "UniProt"
source_id: "Q46798"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303}. Note=Slightly enriched at the septal ring."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ygeR b2865 JW2833"
---

# ygeR

`protein.Q46798`

## Static

- Type: `protein`
- Source: `UniProt:Q46798`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303}. Note=Slightly enriched at the septal ring.

## Enriched Summary

Uncharacterized lipoprotein YgeR ActS (formerly YgeR) contains a lipoprotein signal sequence, a LysM (lysin motif) domain (associated with peptidoglycan binding ) and a LytM (lysostaphin/M23 peptidase) domain (also found in EG12297-MONOMER EnvC, EG12111-MONOMER NlpD and EG10013-MONOMER MepM) . ActS is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). ActS has a degenerate LysM domain and does not have peptidoglycan (PG) hydrolase or endopeptidase activity in vitro . Purified ActS activates the amidases NACMURLALAAMI1-MONOMER AmiA, NACMURLALAAMI2-MONOMER AmiB, and G7458-MONOMER AmiC to digest PG in vitro; ActS interacts physically with AmiC and binds peptidoglycan; ActS appears to function under envelope stress conditions and may function to preferentially activate AmiC (see also ). ActS functions as an amidase activator at low pH; ActS promotes AmiB activity at low pH . Deletion of actS exacerbates the division phenotype of an envC nlpD double null mutant . Over-expression of actS restores cell separation in the envC nlpD double null mutant . actS: amidase activator during stress .

## Annotation

Uncharacterized lipoprotein YgeR

## Outgoing Edges (1)

- `activates` --> [[reaction.ecocyc.RXN-16938|reaction.ecocyc.RXN-16938]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `encodes` <-- [[gene.b2865|gene.b2865]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46798`
- `KEGG:ecj:JW2833;eco:b2865;ecoc:C3026_15720;`
- `GeneID:947352;`
- `GO:GO:0004222; GO:0005886; GO:0009279; GO:0032153; GO:0036460`

## Notes

Uncharacterized lipoprotein YgeR
