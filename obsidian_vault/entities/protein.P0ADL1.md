---
entity_id: "protein.P0ADL1"
entity_type: "protein"
name: "nepI"
source_database: "UniProt"
source_id: "P0ADL1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01189, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nepI yicM b3662 JW5938"
---

# nepI

`protein.P0ADL1`

## Static

- Type: `protein`
- Source: `UniProt:P0ADL1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01189, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Involved in the efflux of purine ribonucleosides, such as inosine and guanosine (PubMed:16040204). Adenosine may also be a substrate (PubMed:16040204). Confers resistance to the hypoxanthine analog 6-mercaptopurine, however the level of resistance is rather low (PubMed:16040204). {ECO:0000269|PubMed:16040204}. The NepI protein is a member of the major facilitator superfamily (MFS) of transporters . nepI encodes a purine ribonucleoside exporter. It was discovered due to its ability to confer resistance to 6-mercaptopurine. Its overexpression in sensitive cells resulted in increased resistance to inosine and guanosine. Overexpression also reduced the growth rate of cells in media with inosine and guanosine as sole carbon source. Inosine accumulation in purine nucleoside phosphorylase deficient cells and the rate of excretion of inosine by an inosine producing strain were increased upon overexpression of nepI . NepI: "nucleoside efflux permease-inosine"

## Biological Role

Catalyzes inosine:proton antiport (reaction.ecocyc.RXN0-18), guanosine:proton antiport (reaction.ecocyc.RXN0-22). Transports Inosine (molecule.C00294), Guanosine (molecule.C00387), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Involved in the efflux of purine ribonucleosides, such as inosine and guanosine (PubMed:16040204). Adenosine may also be a substrate (PubMed:16040204). Confers resistance to the hypoxanthine analog 6-mercaptopurine, however the level of resistance is rather low (PubMed:16040204). {ECO:0000269|PubMed:16040204}.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.RXN0-18|reaction.ecocyc.RXN0-18]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-22|reaction.ecocyc.RXN0-22]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00294|molecule.C00294]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00387|molecule.C00387]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3662|gene.b3662]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADL1`
- `KEGG:ecj:JW5938;eco:b3662;ecoc:C3026_19850;`
- `GeneID:75205376;948213;`
- `GO:GO:0005886; GO:0015211; GO:0015297; GO:0015860; GO:0022857; GO:0055085`

## Notes

Purine ribonucleoside efflux pump NepI (Nucleoside efflux permease-inosine)
