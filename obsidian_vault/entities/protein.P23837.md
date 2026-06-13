---
entity_id: "protein.P23837"
entity_type: "protein"
name: "phoQ"
source_database: "UniProt"
source_id: "P23837"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phoQ b1129 JW1115"
---

# phoQ

`protein.P23837`

## Static

- Type: `protein`
- Source: `UniProt:P23837`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system PhoP/PhoQ involved in adaptation to low Mg(2+) environments and the control of acid resistance genes (By similarity). Also involved in adaptation to hyperosmotic environments, in a Mg(2+)-independent manner (PubMed:29183977). In low periplasmic Mg(2+), PhoQ functions as a membrane-associated protein kinase that undergoes autophosphorylation and subsequently transfers the phosphate to PhoP, resulting in the expression of PhoP-activated genes (PAG) and repression of PhoP-repressed genes (PRG) (By similarity). In high periplasmic Mg(2+), acts as a protein phosphatase that dephosphorylates phospho-PhoP, resulting in the repression of PAG and may lead to expression of some PRG (By similarity). PhoP-regulated transcription is redox-sensitive, being activated when the periplasm becomes more reducing (deletion of dsbA/dsbB, or treatment with dithiothreitol) (PubMed:22267510). MgrB acts between DsbA/DsbB and PhoP/PhoQ in this pathway; the 2 periplasmic Cys residues of MgrB are required for its action on PhoQ, which then acts on PhoP (PubMed:22267510). Mediates magnesium influx to the cytosol by activation of mgtA (PubMed:10464230). Promotes expression of the two-component regulatory system RstA/RstB and transcription of the hemL, mgrB, nagA, slyB, vboR and yrbL genes (PubMed:12813061)...

## Biological Role

Component of bifunctional sensor histidine kinase PhoQ (complex.ecocyc.CPLX0-8168), PhoQ-N-phospho-L-histidine (complex.ecocyc.PHOSPHO-PHOQ). Repressed by mgrB (protein.P64512).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system PhoP/PhoQ involved in adaptation to low Mg(2+) environments and the control of acid resistance genes (By similarity). Also involved in adaptation to hyperosmotic environments, in a Mg(2+)-independent manner (PubMed:29183977). In low periplasmic Mg(2+), PhoQ functions as a membrane-associated protein kinase that undergoes autophosphorylation and subsequently transfers the phosphate to PhoP, resulting in the expression of PhoP-activated genes (PAG) and repression of PhoP-repressed genes (PRG) (By similarity). In high periplasmic Mg(2+), acts as a protein phosphatase that dephosphorylates phospho-PhoP, resulting in the repression of PAG and may lead to expression of some PRG (By similarity). PhoP-regulated transcription is redox-sensitive, being activated when the periplasm becomes more reducing (deletion of dsbA/dsbB, or treatment with dithiothreitol) (PubMed:22267510). MgrB acts between DsbA/DsbB and PhoP/PhoQ in this pathway; the 2 periplasmic Cys residues of MgrB are required for its action on PhoQ, which then acts on PhoP (PubMed:22267510). Mediates magnesium influx to the cytosol by activation of mgtA (PubMed:10464230). Promotes expression of the two-component regulatory system RstA/RstB and transcription of the hemL, mgrB, nagA, slyB, vboR and yrbL genes (PubMed:12813061). In response to osmotic stress promotes transient transcriptional activation of genes in the PhoP regulon, including mgtA, mgrB, phoP, slyB, and borD (PubMed:29183977). Sensing of osmotic stress does not involve the sensor domain, instead resulting from a conformational change induced in the transmembrane domain (PubMed:29183977). Activation of the PhoQ/PhoP system as a result of osmotic stress may contribute to cellular fitness in the host gastrointestinal tract (PubMed:29183977). {ECO:0000250|UniProtKB:P0DM80, ECO:0000269|PubMed:10464230, ECO:0000269|PubMed:12813061, ECO:0000269|PubMed:22267510, ECO:0000269|PubMed:29183977}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8168|complex.ecocyc.CPLX0-8168]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.PHOSPHO-PHOQ|complex.ecocyc.PHOSPHO-PHOQ]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (2)

- `encodes` <-- [[gene.b1129|gene.b1129]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT
- `represses` <-- [[protein.P64512|protein.P64512]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation

## External IDs

- `UniProt:P23837`
- `KEGG:ecj:JW1115;eco:b1129;ecoc:C3026_06795;`
- `GeneID:93776281;946326;`
- `GO:GO:0000155; GO:0000160; GO:0004721; GO:0005524; GO:0005886; GO:0007165; GO:0007234; GO:0010350; GO:0016301; GO:0042802; GO:0046872`
- `EC:2.7.13.3; 3.1.3.-`

## Notes

Sensor protein PhoQ (EC 2.7.13.3) (EC 3.1.3.-) (Sensor histidine protein kinase/phosphatase PhoQ)
