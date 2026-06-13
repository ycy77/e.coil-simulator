---
entity_id: "protein.P0AEG4"
entity_type: "protein"
name: "dsbA"
source_database: "UniProt"
source_id: "P0AEG4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dsbA dsf ppfA b3860 JW3832"
---

# dsbA

`protein.P0AEG4`

## Static

- Type: `protein`
- Source: `UniProt:P0AEG4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: Required for disulfide bond formation in some periplasmic proteins such as PhoA or OmpA. Acts by transferring its disulfide bond to other proteins and is reduced in the process. DsbA is reoxidized by DsbB. Required for pilus biogenesis. PhoP-regulated transcription is redox-sensitive, being activated when the periplasm becomes more reducing (deletion of dsbA/dsbB, treatment with dithiothreitol). MgrB acts between DsbA/DsbB and PhoP/PhoQ in this pathway. {ECO:0000269|PubMed:1429594, ECO:0000269|PubMed:22267510}. DsbA is a periplasmic thiol:disulfide oxidoreductase that promotes protein disulfide bond formation in E. coli K-12. DsbA contains a redox active disulfide bond (Cys30-Cys33) that is catalytically transferred via disulfide exchange to a diverse range of newly translocated protein substrates. Purified DsbA catalyses disulfide bond formation in in vitro translated alkaline phosphatase and stimulates the refolding of reduced bovine RNaseA . DsbA catalyses disulfide reduction in the presence of mild reducing agents in vitro - purified DsbA accelerates the reduction of insulin in the presence of dithiothreitol . dsbA null mutants (dsbA::kan1; ppfA::Tn5) show defects in protein disulfide bond formation . A dsbA null mutant is defective in the synthesis of anaerobically induced c-type cytochromes . dsbA is non-essential in E. coli K-12...

## Biological Role

Catalyzes RXN-21426 (reaction.ecocyc.RXN-21426), RXN0-7450 (reaction.ecocyc.RXN0-7450).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: Required for disulfide bond formation in some periplasmic proteins such as PhoA or OmpA. Acts by transferring its disulfide bond to other proteins and is reduced in the process. DsbA is reoxidized by DsbB. Required for pilus biogenesis. PhoP-regulated transcription is redox-sensitive, being activated when the periplasm becomes more reducing (deletion of dsbA/dsbB, treatment with dithiothreitol). MgrB acts between DsbA/DsbB and PhoP/PhoQ in this pathway. {ECO:0000269|PubMed:1429594, ECO:0000269|PubMed:22267510}.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-21426|reaction.ecocyc.RXN-21426]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7450|reaction.ecocyc.RXN0-7450]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3860|gene.b3860]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEG4`
- `KEGG:ecj:JW3832;eco:b3860;ecoc:C3026_20865;`
- `GeneID:86948491;93778077;948353;`
- `GO:GO:0003756; GO:0015035; GO:0030288; GO:0071236`

## Notes

Thiol:disulfide interchange protein DsbA
