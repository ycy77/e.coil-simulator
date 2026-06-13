---
entity_id: "protein.P0C0V0"
entity_type: "protein"
name: "degP"
source_database: "UniProt"
source_id: "P0C0V0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:9083020}; Peripheral membrane protein {ECO:0000269|PubMed:9083020}; Cytoplasmic side {ECO:0000269|PubMed:9083020}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "degP htrA ptd b0161 JW0157"
---

# degP

`protein.P0C0V0`

## Static

- Type: `protein`
- Source: `UniProt:P0C0V0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:9083020}; Peripheral membrane protein {ECO:0000269|PubMed:9083020}; Cytoplasmic side {ECO:0000269|PubMed:9083020}.

## Enriched Summary

FUNCTION: DegP acts as a chaperone at low temperatures but switches to a peptidase (heat shock protein) at higher temperatures (PubMed:10319814). Degrades transiently denatured and unfolded or misfolded proteins which accumulate in the periplasm following heat shock or other stress conditions (PubMed:16303867). DegP is efficient with Val-Xaa and Ile-Xaa peptide bonds, suggesting a preference for beta-branched side chain amino acids (PubMed:8830688). Only unfolded proteins devoid of disulfide bonds appear capable of being cleaved, thereby preventing non-specific proteolysis of folded proteins (PubMed:8830688). Its proteolytic activity is essential for the survival of cells at elevated temperatures (PubMed:7557477). It can degrade IciA, Ada, casein, globin and PapA. DegP shares specificity with DegQ (PubMed:8830688). DegP is also involved in the biogenesis of partially folded outer-membrane proteins (OMP). {ECO:0000269|PubMed:10319814, ECO:0000269|PubMed:12730160, ECO:0000269|PubMed:16303867, ECO:0000269|PubMed:18496527, ECO:0000269|PubMed:18505836, ECO:0000269|PubMed:2180903, ECO:0000269|PubMed:7557477, ECO:0000269|PubMed:8830688}.

## Biological Role

Component of periplasmic serine endoprotease DegP (complex.ecocyc.CPLX0-2921).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: DegP acts as a chaperone at low temperatures but switches to a peptidase (heat shock protein) at higher temperatures (PubMed:10319814). Degrades transiently denatured and unfolded or misfolded proteins which accumulate in the periplasm following heat shock or other stress conditions (PubMed:16303867). DegP is efficient with Val-Xaa and Ile-Xaa peptide bonds, suggesting a preference for beta-branched side chain amino acids (PubMed:8830688). Only unfolded proteins devoid of disulfide bonds appear capable of being cleaved, thereby preventing non-specific proteolysis of folded proteins (PubMed:8830688). Its proteolytic activity is essential for the survival of cells at elevated temperatures (PubMed:7557477). It can degrade IciA, Ada, casein, globin and PapA. DegP shares specificity with DegQ (PubMed:8830688). DegP is also involved in the biogenesis of partially folded outer-membrane proteins (OMP). {ECO:0000269|PubMed:10319814, ECO:0000269|PubMed:12730160, ECO:0000269|PubMed:16303867, ECO:0000269|PubMed:18496527, ECO:0000269|PubMed:18505836, ECO:0000269|PubMed:2180903, ECO:0000269|PubMed:7557477, ECO:0000269|PubMed:8830688}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2921|complex.ecocyc.CPLX0-2921]] `EcoCyc` `database` - EcoCyc component coefficient=12 | EcoCyc protcplxs.col coefficient=12

## Incoming Edges (1)

- `encodes` <-- [[gene.b0161|gene.b0161]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C0V0`
- `KEGG:ecj:JW0157;eco:b0161;ecoc:C3026_00735;`
- `GeneID:93777263;947139;`
- `GO:GO:0004252; GO:0005886; GO:0006457; GO:0006508; GO:0006515; GO:0006979; GO:0008233; GO:0008236; GO:0009266; GO:0009408; GO:0030288; GO:0042597; GO:0042802`
- `EC:3.4.21.107`

## Notes

Periplasmic serine endoprotease DegP (EC 3.4.21.107) (Heat shock protein DegP) (Protease Do)
