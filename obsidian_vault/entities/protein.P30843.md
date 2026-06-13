---
entity_id: "protein.P30843"
entity_type: "protein"
name: "basR"
source_database: "UniProt"
source_id: "P30843"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "basR pmrA b4113 JW4074"
---

# basR

`protein.P30843`

## Static

- Type: `protein`
- Source: `UniProt:P30843`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system BasS/BasR. BasR induces the transcription of the ugd, ais, arnBCADTEF and eptA-basRS loci, all involved in resistance to polymyxin (By similarity). {ECO:0000250}. The transcriptional regulatory protein BasR appears to be involved in resistance to colistin and to the bacteriocin plantaricin BM-1 . Proteome analysis suggested that BasR directly or indirectly represses the expression of 26 proteins and activates the expression of 58 proteins involved in several cellular processes, including the tricarboxylic acid cycle . BasR is part of the two-component BasS/BasR signal transduction system . BasS functions as a membrane-associated protein kinase that phosphorylates BasR in response to elevated levels of Fe(III) which can permeabilize the outer membrane and result in cell death . Phosphorylation of BasR increases the affinity for its specific DNA binding sites, leading to the transcriptional expression of several genes involved in modification of lipopolysaccharide to prevent excessiveFe(III) binding . basR expression is necessary for lipid A modifications when E. coli is grown in low concentrations of Mg2+. These modifications are necessary for the survival of cells exposed to polymyxin B . BasR is not an essential protein . Deletion of basR resulted in susceptibility to cell-killing by elevated levels of Fe(III)...

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system BasS/BasR. BasR induces the transcription of the ugd, ais, arnBCADTEF and eptA-basRS loci, all involved in resistance to polymyxin (By similarity). {ECO:0000250}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (21)

- `activates` --> [[gene.b0460|gene.b0460]] `RegulonDB` `S` - regulator=BasR; target=hha; function=+
- `activates` --> [[gene.b0461|gene.b0461]] `RegulonDB` `S` - regulator=BasR; target=tomB; function=+
- `activates` --> [[gene.b1037|gene.b1037]] `RegulonDB` `S` - regulator=BasR; target=csgG; function=+
- `activates` --> [[gene.b1038|gene.b1038]] `RegulonDB` `S` - regulator=BasR; target=csgF; function=+
- `activates` --> [[gene.b1039|gene.b1039]] `RegulonDB` `S` - regulator=BasR; target=csgE; function=+
- `activates` --> [[gene.b1040|gene.b1040]] `RegulonDB` `S` - regulator=BasR; target=csgD; function=+
- `activates` --> [[gene.b1552|gene.b1552]] `RegulonDB` `S` - regulator=BasR; target=cspI; function=+
- `activates` --> [[gene.b2253|gene.b2253]] `RegulonDB` `S` - regulator=BasR; target=arnB; function=+
- `activates` --> [[gene.b2254|gene.b2254]] `RegulonDB` `S` - regulator=BasR; target=arnC; function=+
- `activates` --> [[gene.b2255|gene.b2255]] `RegulonDB` `S` - regulator=BasR; target=arnA; function=+
- `activates` --> [[gene.b2256|gene.b2256]] `RegulonDB` `S` - regulator=BasR; target=arnD; function=+
- `activates` --> [[gene.b2257|gene.b2257]] `RegulonDB` `S` - regulator=BasR; target=arnT; function=+
- `activates` --> [[gene.b2258|gene.b2258]] `RegulonDB` `S` - regulator=BasR; target=arnF; function=+
- `activates` --> [[gene.b3025|gene.b3025]] `RegulonDB` `S` - regulator=BasR; target=qseB; function=+
- `activates` --> [[gene.b3026|gene.b3026]] `RegulonDB` `S` - regulator=BasR; target=qseC; function=+
- `activates` --> [[gene.b4042|gene.b4042]] `RegulonDB` `C` - regulator=BasR; target=dgkA; function=+
- `activates` --> [[gene.b4114|gene.b4114]] `RegulonDB` `C` - regulator=BasR; target=eptA; function=+
- `activates` --> [[gene.b4312|gene.b4312]] `RegulonDB` `S` - regulator=BasR; target=fimB; function=+
- `activates` --> [[gene.b4544|gene.b4544]] `RegulonDB` `S` - regulator=BasR; target=arnE; function=+
- `represses` --> [[gene.b1014|gene.b1014]] `RegulonDB` `S` - regulator=BasR; target=putA; function=-
- `represses` --> [[gene.b3207|gene.b3207]] `RegulonDB` `S` - regulator=BasR; target=yrbL; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b4113|gene.b4113]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30843`
- `KEGG:ecj:JW4074;eco:b4113;ecoc:C3026_22225;`
- `GeneID:948631;`
- `GO:GO:0000156; GO:0000160; GO:0000976; GO:0005829; GO:0006355; GO:0010041; GO:0032993; GO:0046677`

## Notes

Transcriptional regulatory protein BasR
