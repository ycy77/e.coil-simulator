---
entity_id: "protein.P07102"
entity_type: "protein"
name: "appA"
source_database: "UniProt"
source_id: "P07102"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:10696472, ECO:0000269|PubMed:1429631, ECO:0000269|PubMed:8387749, ECO:0000269|PubMed:8407904}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "appA b0980 JW0963"
---

# appA

`protein.P07102`

## Static

- Type: `protein`
- Source: `UniProt:P07102`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:10696472, ECO:0000269|PubMed:1429631, ECO:0000269|PubMed:8387749, ECO:0000269|PubMed:8407904}.

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of phytate (or myo-inositol hexakisphosphate, an indigestible organic form of phosphorus that is found in many plant tissues) to myo-inositol and inorganic phosphate (PubMed:10696472, PubMed:11035187, PubMed:30712472, PubMed:8387749, Ref.8). Dephosphorylates phytate in a stereospecific way by sequential removal of phosphate groups to produce myo-inositol 2-monophosphate (PubMed:11035187). Also shows phosphoanhydride phosphatase activity and hydrolyzes the distal phosphoryl residues of GTP, the 5'-beta-phosphoryl residue of the regulatory nucleotide ppGpp and tripolyphosphates (PubMed:1429631, PubMed:6282821, PubMed:8407904). Does not split most phosphomonoesters with the exception of the synthetic substrate p-nitrophenyl phosphate (pNPP), 2,3-bisphosphoglycerate and fructose 1,6-bisphosphate (PubMed:10696472, PubMed:1429631, PubMed:6282821, PubMed:8387749, PubMed:8407904, Ref.8). {ECO:0000269|PubMed:10696472, ECO:0000269|PubMed:11035187, ECO:0000269|PubMed:1429631, ECO:0000269|PubMed:30712472, ECO:0000269|PubMed:6282821, ECO:0000269|PubMed:8387749, ECO:0000269|PubMed:8407904, ECO:0000269|Ref.8}. appA encodes a periplasmic protein with phosphoanhydride phosphatase and multiple inositol-polyphosphate phosphatase activity. The purified protein (initially isolated from E...

## Biological Role

Catalyzes riboflavin-5-phosphate phosphohydrolase (reaction.R00548), phosphate-monoester phosphohydrolase (reaction.R00626), glycerone phosphate phosphohydrolase (reaction.R01010), thiamin monophosphate phosphohydrolase (reaction.R02135), 1-acyl-sn-glycerol 3-phosphate phosphohydrolase (reaction.R11527). Component of periplasmic phosphoanhydride phosphatase/multiple inositol-polyphosphate phosphatase (complex.ecocyc.CPLX-722).

## Enriched Pathways

- `eco00562` Inositol phosphate metabolism (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of phytate (or myo-inositol hexakisphosphate, an indigestible organic form of phosphorus that is found in many plant tissues) to myo-inositol and inorganic phosphate (PubMed:10696472, PubMed:11035187, PubMed:30712472, PubMed:8387749, Ref.8). Dephosphorylates phytate in a stereospecific way by sequential removal of phosphate groups to produce myo-inositol 2-monophosphate (PubMed:11035187). Also shows phosphoanhydride phosphatase activity and hydrolyzes the distal phosphoryl residues of GTP, the 5'-beta-phosphoryl residue of the regulatory nucleotide ppGpp and tripolyphosphates (PubMed:1429631, PubMed:6282821, PubMed:8407904). Does not split most phosphomonoesters with the exception of the synthetic substrate p-nitrophenyl phosphate (pNPP), 2,3-bisphosphoglycerate and fructose 1,6-bisphosphate (PubMed:10696472, PubMed:1429631, PubMed:6282821, PubMed:8387749, PubMed:8407904, Ref.8). {ECO:0000269|PubMed:10696472, ECO:0000269|PubMed:11035187, ECO:0000269|PubMed:1429631, ECO:0000269|PubMed:30712472, ECO:0000269|PubMed:6282821, ECO:0000269|PubMed:8387749, ECO:0000269|PubMed:8407904, ECO:0000269|Ref.8}.

## Pathways

- `eco00562` Inositol phosphate metabolism (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.R00548|reaction.R00548]] `KEGG` `database` - via EC:3.1.3.2
- `catalyzes` --> [[reaction.R00626|reaction.R00626]] `KEGG` `database` - via EC:3.1.3.2
- `catalyzes` --> [[reaction.R01010|reaction.R01010]] `KEGG` `database` - via EC:3.1.3.2
- `catalyzes` --> [[reaction.R02135|reaction.R02135]] `KEGG` `database` - via EC:3.1.3.2
- `catalyzes` --> [[reaction.R11527|reaction.R11527]] `KEGG` `database` - via EC:3.1.3.2
- `is_component_of` --> [[complex.ecocyc.CPLX-722|complex.ecocyc.CPLX-722]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0980|gene.b0980]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07102`
- `KEGG:ecj:JW0963;eco:b0980;ecoc:C3026_05980;`
- `GeneID:93776432;946206;`
- `GO:GO:0003924; GO:0008252; GO:0016036; GO:0030288; GO:0050308; GO:0052745; GO:0071454`
- `EC:3.1.3.-; 3.6.1.-`

## Notes

Phytase AppA (EC 3.1.3.-) (6-phytase) (Histidine acid phosphatase phytase) (HAP phytase) (Myo-inositol hexakisphosphate phosphohydrolase) (Phosphoanhydride phosphatase) (EC 3.6.1.-) (pH 2.5 acid phosphatase) (Acid phosphatase) (EC 3.1.3.-)
