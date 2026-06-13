---
entity_id: "protein.P69783"
entity_type: "protein"
name: "crr"
source_database: "UniProt"
source_id: "P69783"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "crr gsr iex tgs treD b2417 JW2410"
---

# crr

`protein.P69783`

## Static

- Type: `protein`
- Source: `UniProt:P69783`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane (PubMed:17158705, PubMed:3129430). The enzyme II complex composed of PtsG and Crr is involved in glucose transport (PubMed:2657735). The non-phosphorylated EIII-Glc is an inhibitor for uptake of certain sugars such as maltose, melibiose, lactose, and glycerol. Phosphorylated EIII-Glc, however, may be an activator for adenylate cyclase. It is an important regulatory protein for cell metabolism (PubMed:789369). {ECO:0000269|PubMed:2657735, ECO:0000269|PubMed:3129430, ECO:0000269|PubMed:789369, ECO:0000305|PubMed:17158705}. EIIAGlc is an intermediate phosphotransfer protein in the uptake and phosphorylation of glucose , N-acetylmuramic acid and trehalose and also probably interacts with MalX - a PTS permease whose physiological substrate is unclear . EIIAGlc accepts a phosphoryl group from PTSH-MONOMER "PtsH" and transfers it to the the EIIB domain of the sugar PTS permeases. EIIAGlc is phosphorylated by phosphoenolpyruvate (PEP) in a reaction requiring PtsH and PTSI-MONOMER "PtsI". EIIAGlc is phosphorylated at the N3 position of His90...

## Biological Role

Component of glucose-specific PTS enzyme II (complex.ecocyc.CPLX-157), trehalose-specific PTS enzyme II (complex.ecocyc.CPLX-168), N-acetylmuramic acid-specific PTS enzyme II (complex.ecocyc.CPLX0-7).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane (PubMed:17158705, PubMed:3129430). The enzyme II complex composed of PtsG and Crr is involved in glucose transport (PubMed:2657735). The non-phosphorylated EIII-Glc is an inhibitor for uptake of certain sugars such as maltose, melibiose, lactose, and glycerol. Phosphorylated EIII-Glc, however, may be an activator for adenylate cyclase. It is an important regulatory protein for cell metabolism (PubMed:789369). {ECO:0000269|PubMed:2657735, ECO:0000269|PubMed:3129430, ECO:0000269|PubMed:789369, ECO:0000305|PubMed:17158705}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.CPLX-157|complex.ecocyc.CPLX-157]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX-168|complex.ecocyc.CPLX-168]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-7|complex.ecocyc.CPLX0-7]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `represses` --> [[reaction.ecocyc.GLYCEROL-KIN-RXN|reaction.ecocyc.GLYCEROL-KIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `encodes` <-- [[gene.b2417|gene.b2417]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69783`
- `KEGG:ecj:JW2410;eco:b2417;ecoc:C3026_13435;`
- `GeneID:86860560;93774714;946880;`
- `GO:GO:0005829; GO:0009401; GO:0016020; GO:0016301; GO:0034763; GO:0043610; GO:0045912; GO:0046872; GO:1902344; GO:1902495; GO:1990154`

## Notes

PTS system glucose-specific EIIA component (EIIA-Glc) (EIII-Glc) (Glucose-specific phosphotransferase enzyme IIA component)
