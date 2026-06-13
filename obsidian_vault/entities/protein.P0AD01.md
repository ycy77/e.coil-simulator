---
entity_id: "protein.P0AD01"
entity_type: "protein"
name: "dcuR"
source_database: "UniProt"
source_id: "P0AD01"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dcuR yjdG b4124 JW4085"
---

# dcuR

`protein.P0AD01`

## Static

- Type: `protein`
- Source: `UniProt:P0AD01`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system DcuR/DcuS. Involved in the C4-dicarboxylate-stimulated regulation of the genes encoding the anaerobic fumarate respiratory system (frdABCD; nuoAN; dcuB; dcuC; sdhCDAB; etc.). Weakly regulates the aerobic C4-dicarboxylate transporter dctA.

## Biological Role

Component of DNA-binding transcriptional activator DcuR-phosphorylated (complex.ecocyc.CPLX0-7721).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system DcuR/DcuS. Involved in the C4-dicarboxylate-stimulated regulation of the genes encoding the anaerobic fumarate respiratory system (frdABCD; nuoAN; dcuB; dcuC; sdhCDAB; etc.). Weakly regulates the aerobic C4-dicarboxylate transporter dctA.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (10)

- `activates` --> [[gene.b0619|gene.b0619]] `RegulonDB` `S` - regulator=DcuR; target=dpiB; function=+
- `activates` --> [[gene.b0620|gene.b0620]] `RegulonDB` `S` - regulator=DcuR; target=dpiA; function=+
- `activates` --> [[gene.b3528|gene.b3528]] `RegulonDB` `S` - regulator=DcuR; target=dctA; function=+
- `activates` --> [[gene.b4122|gene.b4122]] `RegulonDB` `S` - regulator=DcuR; target=fumB; function=+
- `activates` --> [[gene.b4123|gene.b4123]] `RegulonDB` `S` - regulator=DcuR; target=dcuB; function=+
- `activates` --> [[gene.b4151|gene.b4151]] `RegulonDB` `S` - regulator=DcuR; target=frdD; function=+
- `activates` --> [[gene.b4152|gene.b4152]] `RegulonDB` `S` - regulator=DcuR; target=frdC; function=+
- `activates` --> [[gene.b4153|gene.b4153]] `RegulonDB` `S` - regulator=DcuR; target=frdB; function=+
- `activates` --> [[gene.b4154|gene.b4154]] `RegulonDB` `S` - regulator=DcuR; target=frdA; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7721|complex.ecocyc.CPLX0-7721]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4124|gene.b4124]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AD01`
- `KEGG:ecj:JW4085;eco:b4124;ecoc:C3026_22290;`
- `GeneID:75169642;75203994;948640;`
- `GO:GO:0000156; GO:0000160; GO:0001216; GO:0003677; GO:0005737; GO:0006351; GO:0042803; GO:0045893`

## Notes

Transcriptional regulatory protein DcuR
