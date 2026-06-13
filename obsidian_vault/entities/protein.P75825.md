---
entity_id: "protein.P75825"
entity_type: "protein"
name: "hcp"
source_database: "UniProt"
source_id: "P75825"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00069}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hcp ybjW b0873 JW0857"
---

# hcp

`protein.P75825`

## Static

- Type: `protein`
- Source: `UniProt:P75825`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00069}.

## Enriched Summary

FUNCTION: Catalyzes the reduction of hydroxylamine to form NH(3) and H(2)O. Is also able to reduce hydroxylamine analogs such as methylhydroxylamine and hydroxyquinone. Might have a role as a scavenger of potentially toxic by-products of nitrate metabolism. {ECO:0000255|HAMAP-Rule:MF_00069, ECO:0000269|PubMed:10651802, ECO:0000269|PubMed:12374823}. The hybrid cluster protein (HCP) is a high-affinity NO reductase that is responsible for the majority of NO detoxification at low concentrations of NO . HCP exhibits hydroxylamine reductase activity, possibly functioning as a scavenger of toxic by-products of nitrogen metabolism . HCP was originally suggested to be involved in nitrate-and/or nitrite respiration based on its regulation . HCP contains iron-sulfur clusters of the [2Fe-2S] and [4Fe-2S-2O] type and is reduced by the Hcr NADH oxidoreductase . The properties of electron transfer in the Hcr-HCP system have been studied . Growth of an hcp hcr mutant in a strain background that lacks known NO reductases and nitrite reductases (i.e. ΔnirBD, nrfAB, norVW) is inhibited in the presence of nitrate or nitrite . HCP is produced during anaerobic growth in the presence of nitrate or nitrite . Expression is induced by NarL, NarP, OxyR and FNR and repressed by EG11212-MONOMER NsrR...

## Biological Role

Catalyzes ammonia:NAD+ oxidoreductase; (reaction.R00143), ammonia:acceptor oxidoreductase (reaction.R00284), HYDROXYLAMINE-REDUCTASE-RXN (reaction.ecocyc.HYDROXYLAMINE-REDUCTASE-RXN). Bound by a [4Fe-2O-2S] iron-sulfur cluster (molecule.ecocyc.4Fe-2O-2S-Cluster), a [2Fe-2S] iron-sulfur cluster (molecule.ecocyc.CPD-6).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the reduction of hydroxylamine to form NH(3) and H(2)O. Is also able to reduce hydroxylamine analogs such as methylhydroxylamine and hydroxyquinone. Might have a role as a scavenger of potentially toxic by-products of nitrate metabolism. {ECO:0000255|HAMAP-Rule:MF_00069, ECO:0000269|PubMed:10651802, ECO:0000269|PubMed:12374823}.

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00143|reaction.R00143]] `KEGG` `database` - via EC:1.7.99.1
- `catalyzes` --> [[reaction.R00284|reaction.R00284]] `KEGG` `database` - via EC:1.7.99.1
- `catalyzes` --> [[reaction.ecocyc.HYDROXYLAMINE-REDUCTASE-RXN|reaction.ecocyc.HYDROXYLAMINE-REDUCTASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.ecocyc.4Fe-2O-2S-Cluster|molecule.ecocyc.4Fe-2O-2S-Cluster]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-6|molecule.ecocyc.CPD-6]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0873|gene.b0873]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75825`
- `KEGG:ecj:JW0857;eco:b0873;ecoc:C3026_05425;`
- `GeneID:946592;`
- `GO:GO:0004601; GO:0005737; GO:0016491; GO:0042542; GO:0046210; GO:0046872; GO:0050418; GO:0051537`
- `EC:1.7.99.1`

## Notes

Hydroxylamine reductase (EC 1.7.99.1) (Hybrid-cluster protein) (HCP) (Prismane protein)
