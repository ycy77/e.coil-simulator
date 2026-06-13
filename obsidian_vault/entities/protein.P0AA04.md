---
entity_id: "protein.P0AA04"
entity_type: "protein"
name: "ptsH"
source_database: "UniProt"
source_id: "P0AA04"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ptsH hpr b2415 JW2408"
---

# ptsH

`protein.P0AA04`

## Static

- Type: `protein`
- Source: `UniProt:P0AA04`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: General (non sugar-specific) component of the phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS). This major carbohydrate active-transport system catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The phosphoryl group from phosphoenolpyruvate (PEP) is transferred to the phosphoryl carrier protein HPr by enzyme I. Phospho-HPr then transfers it to the PTS EIIA domain. The bacterial phosphoenolpyruvate:sugar phosphotransferase system involves a series of reactions in which phosphorylated protein intermediates are formed. Histidine-containing protein (HPr) is phosphorylated on the Nπ position of the imidazole ring of His15 by CPLX0-7938 "PTS enzyme I" and acts as a phosphoryl donor to the sugar-specific enzymes IIA . HPr (histidine containing protein ) is one of two sugar-non-specific protein constituents of the phosphoenolpyruvate:sugar phosphotransferase system (PTSsugar). It accepts a phosphoryl group from phosphorylated Enzyme I (PtsI-P) and then transfers it to the EIIA domain of any one of the many sugar-specific enzymes (collectively known as Enzymes II) of the PTSsugar (reviewed in ). HPr is a small monomeric, single domain, protein that is relatively heat stable . HPr is phosphorylated at the N-1 position of histidine residue 15 (His-15)...

## Enriched Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: General (non sugar-specific) component of the phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS). This major carbohydrate active-transport system catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The phosphoryl group from phosphoenolpyruvate (PEP) is transferred to the phosphoryl carrier protein HPr by enzyme I. Phospho-HPr then transfers it to the PTS EIIA domain.

## Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (6)

- `activates` --> [[reaction.ecocyc.6PFRUCTPHOS-RXN|reaction.ecocyc.6PFRUCTPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.GLUCOSAMINE-6-P-DEAMIN-RXN|reaction.ecocyc.GLUCOSAMINE-6-P-DEAMIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.GLYCOPHOSPHORYL-RXN|reaction.ecocyc.GLYCOPHOSPHORYL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.PEPDEPHOS-RXN|reaction.ecocyc.PEPDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ADENYL-KIN-RXN|reaction.ecocyc.ADENYL-KIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5461|reaction.ecocyc.RXN0-5461]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `encodes` <-- [[gene.b2415|gene.b2415]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA04`
- `KEGG:ecj:JW2408;eco:b2415;ecoc:C3026_13425;`
- `GeneID:946886;99706872;`
- `GO:GO:0004857; GO:0005829; GO:0008047; GO:0009401; GO:0016775; GO:0030234; GO:0043609; GO:0045152; GO:0045819`

## Notes

Phosphocarrier protein HPr (Histidine-containing protein)
