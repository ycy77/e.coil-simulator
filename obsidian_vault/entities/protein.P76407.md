---
entity_id: "protein.P76407"
entity_type: "protein"
name: "yegS"
source_database: "UniProt"
source_id: "P76407"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:17351295}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yegS b2086 JW2070"
---

# yegS

`protein.P76407`

## Static

- Type: `protein`
- Source: `UniProt:P76407`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:17351295}.

## Enriched Summary

FUNCTION: In vitro phosphorylates phosphatidylglycerol but not diacylglycerol; the in vivo substrate is unknown. YegS is a lipid kinase with phosphatidylglycerol kinase activity in vitro . It shows sequence similarity to a family of eukaryotic non-protein kinases . The physiological role of YegS is unknown, but a possible role in the response to acid stress has been proposed . A crystal structure of YegS has been determined at 1.9 Å resolution; the protein shows structural similarity to a family of NAD kinases . In an experimental evolution experiment for growth under glucose limitation in a chemostat, inactivation of yegS conferred an increase in fitness .

## Biological Role

Catalyzes RXN0-5223 (reaction.ecocyc.RXN0-5223). Bound by Ca2+ (molecule.ecocyc.CA_2).

## Annotation

FUNCTION: In vitro phosphorylates phosphatidylglycerol but not diacylglycerol; the in vivo substrate is unknown.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5223|reaction.ecocyc.RXN0-5223]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2086|gene.b2086]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76407`
- `KEGG:ecj:JW2070;eco:b2086;ecoc:C3026_11715;`
- `GeneID:946626;`
- `GO:GO:0000287; GO:0001727; GO:0005524; GO:0005737; GO:0006665; GO:0008654; GO:0016020`
- `EC:2.7.1.-`

## Notes

Lipid kinase YegS (EC 2.7.1.-)
