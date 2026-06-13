---
entity_id: "protein.P23836"
entity_type: "protein"
name: "phoP"
source_database: "UniProt"
source_id: "P23836"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phoP b1130 JW1116"
---

# phoP

`protein.P23836`

## Static

- Type: `protein`
- Source: `UniProt:P23836`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system PhoP/PhoQ involved in adaptation to low Mg(2+) environments and the control of acid resistance genes. In low periplasmic Mg(2+), PhoQ phosphorylates PhoP, resulting in the expression of PhoP-activated genes (PAG) and repression of PhoP-repressed genes (PRG). In high periplasmic Mg(2+), PhoQ dephosphorylates phospho-PhoP, resulting in the repression of PAG and may lead to expression of some PRG (By similarity). Mediates magnesium influx to the cytosol by activation of MgtA. Promotes expression of the two-component regulatory system rstA/rstB and transcription of the hemL, mgrB, nagA, slyB, vboR and yrbL genes. {ECO:0000250, ECO:0000269|PubMed:10464230}. PhoP is a dual transcriptional regulator that is activated in response to low extracellular levels of divalent cations, e.g., magnesium or calcium . In Escherichia coli K-12, PhoP activates transcription of a large collection of genes involved in Mg2+ homeostasis, resistance to antimicrobial peptides, acid resistance, and LPS modification . A mutation in the phoPQ genes generates cellular resistance to trimethoprim and nitrofurantoin under different growth conditions...

## Biological Role

Repressed by mgrB (protein.P64512).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system PhoP/PhoQ involved in adaptation to low Mg(2+) environments and the control of acid resistance genes. In low periplasmic Mg(2+), PhoQ phosphorylates PhoP, resulting in the expression of PhoP-activated genes (PAG) and repression of PhoP-repressed genes (PRG). In high periplasmic Mg(2+), PhoQ dephosphorylates phospho-PhoP, resulting in the repression of PAG and may lead to expression of some PRG (By similarity). Mediates magnesium influx to the cytosol by activation of MgtA. Promotes expression of the two-component regulatory system rstA/rstB and transcription of the hemL, mgrB, nagA, slyB, vboR and yrbL genes. {ECO:0000250, ECO:0000269|PubMed:10464230}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (29)

- `activates` --> [[gene.b0154|gene.b0154]] `RegulonDB` `S` - regulator=PhoP; target=hemL; function=+
- `activates` --> [[gene.b0557|gene.b0557]] `RegulonDB` `S` - regulator=PhoP; target=borD; function=+
- `activates` --> [[gene.b0565|gene.b0565]] `RegulonDB` `C` - regulator=PhoP; target=ompT; function=+
- `activates` --> [[gene.b0677|gene.b0677]] `RegulonDB` `S` - regulator=PhoP; target=nagA; function=+
- `activates` --> [[gene.b1129|gene.b1129]] `RegulonDB` `S` - regulator=PhoP; target=phoQ; function=-+
- `activates` --> [[gene.b1130|gene.b1130]] `RegulonDB` `S` - regulator=PhoP; target=phoP; function=-+
- `activates` --> [[gene.b1608|gene.b1608]] `RegulonDB` `S` - regulator=PhoP; target=rstA; function=+
- `activates` --> [[gene.b1609|gene.b1609]] `RegulonDB` `S` - regulator=PhoP; target=rstB; function=+
- `activates` --> [[gene.b1641|gene.b1641]] `RegulonDB` `S` - regulator=PhoP; target=slyB; function=-+
- `activates` --> [[gene.b1826|gene.b1826]] `RegulonDB` `S` - regulator=PhoP; target=mgrB; function=+
- `activates` --> [[gene.b2777|gene.b2777]] `RegulonDB` `S` - regulator=PhoP; target=queE; function=+
- `activates` --> [[gene.b3207|gene.b3207]] `RegulonDB` `S` - regulator=PhoP; target=yrbL; function=+
- `activates` --> [[gene.b3508|gene.b3508]] `RegulonDB` `S` - regulator=PhoP; target=yhiD; function=+
- `activates` --> [[gene.b3509|gene.b3509]] `RegulonDB` `S` - regulator=PhoP; target=hdeB; function=+
- `activates` --> [[gene.b3510|gene.b3510]] `RegulonDB` `S` - regulator=PhoP; target=hdeA; function=+
- `activates` --> [[gene.b3511|gene.b3511]] `RegulonDB` `S` - regulator=PhoP; target=hdeD; function=+
- `activates` --> [[gene.b3515|gene.b3515]] `RegulonDB` `S` - regulator=PhoP; target=gadW; function=+
- `activates` --> [[gene.b4242|gene.b4242]] `RegulonDB` `C` - regulator=PhoP; target=mgtA; function=+
- `activates` --> [[gene.b4624|gene.b4624]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4702|gene.b4702]] `RegulonDB` `C` - regulator=PhoP; target=mgtL; function=+
- `represses` --> [[gene.b0881|gene.b0881]] `RegulonDB` `S` - regulator=PhoP; target=clpS; function=-
- `represses` --> [[gene.b0953|gene.b0953]] `RegulonDB|EcoCyc` `S` - regulator=PhoP; target=rmf; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1129|gene.b1129]] `RegulonDB` `S` - regulator=PhoP; target=phoQ; function=-+
- `represses` --> [[gene.b1130|gene.b1130]] `RegulonDB` `S` - regulator=PhoP; target=phoP; function=-+
- `represses` --> [[gene.b1499|gene.b1499]] `RegulonDB` `S` - regulator=PhoP; target=ydeO; function=-
- `represses` --> [[gene.b1500|gene.b1500]] `RegulonDB` `S` - regulator=PhoP; target=safA; function=-
- `represses` --> [[gene.b1641|gene.b1641]] `RegulonDB` `S` - regulator=PhoP; target=slyB; function=-+
- `represses` --> [[gene.b3995|gene.b3995]] `RegulonDB|EcoCyc` `S` - regulator=PhoP; target=rsd; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4241|gene.b4241]] `RegulonDB` `C` - regulator=PhoP; target=treR; function=-

## Incoming Edges (2)

- `encodes` <-- [[gene.b1130|gene.b1130]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT
- `represses` <-- [[protein.P64512|protein.P64512]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation

## External IDs

- `UniProt:P23836`
- `KEGG:ecj:JW1116;eco:b1130;ecoc:C3026_06800;`
- `GeneID:945697;`
- `GO:GO:0000156; GO:0000976; GO:0001216; GO:0005829; GO:0006355; GO:0032993; GO:0042802; GO:0045893`

## Notes

Transcriptional regulatory protein PhoP
