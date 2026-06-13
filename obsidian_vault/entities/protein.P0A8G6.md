---
entity_id: "protein.P0A8G6"
entity_type: "protein"
name: "wrbA"
source_database: "UniProt"
source_id: "P0A8G6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wrbA b1004 JW0989"
---

# wrbA

`protein.P0A8G6`

## Static

- Type: `protein`
- Source: `UniProt:P0A8G6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: It seems to function in response to environmental stress when various electron transfer chains are affected or when the environment is highly oxidizing. It reduces quinones to the hydroquinone state to prevent interaction of the semiquinone with O2 and production of superoxide. It prefers NADH over NADPH. {ECO:0000269|PubMed:16672604, ECO:0000269|PubMed:9694845}. The purified WrbA protein has NAD(P)H:quinone oxidoreductase activity . WrbA is related to the flavodoxin family of proteins . Unlike the flavodoxins, WrbA does not have a stabilized semiquinone state. It rapidly takes up two electrons, generating the fully reduced form . Purified WrbA protein binds one FMN per monomer with a binding constant of 2 µM at room temperature, which is weaker than that of typical flavodoxins . Binding of FMN appears to be pH-dependent , and it increases the thermal stability and promotes tetramerization of WrbA . Despite the extensive work on this enzyme, its natural substrate and physiological role remain opaque. A new crystal structure combined with a novel application of quantum mechanical calculations can now constrain computational docking attempts with potential substrates . WrbA is a multimer in solution, existing in an equilibrium between the dimeric and tetrameric form . Crystal structures show WrbA to be a dimer of dimers...

## Biological Role

Component of NAD(P)H:quinone oxidoreductase (complex.ecocyc.CPLX0-7632).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: It seems to function in response to environmental stress when various electron transfer chains are affected or when the environment is highly oxidizing. It reduces quinones to the hydroquinone state to prevent interaction of the semiquinone with O2 and production of superoxide. It prefers NADH over NADPH. {ECO:0000269|PubMed:16672604, ECO:0000269|PubMed:9694845}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7632|complex.ecocyc.CPLX0-7632]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1004|gene.b1004]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8G6`
- `KEGG:ecj:JW0989;eco:b1004;ecoc:C3026_06110;`
- `GeneID:93776407;947263;`
- `GO:GO:0003955; GO:0005829; GO:0006979; GO:0008753; GO:0010181; GO:0016020; GO:0032991; GO:0042802; GO:0050136; GO:0050660; GO:0050661; GO:0051287`
- `EC:1.6.5.2`

## Notes

NAD(P)H dehydrogenase (quinone) (EC 1.6.5.2) (Flavoprotein WrbA) (NAD(P)H:quinone oxidoreductase) (NQO)
