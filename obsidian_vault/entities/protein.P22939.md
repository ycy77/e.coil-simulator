---
entity_id: "protein.P22939"
entity_type: "protein"
name: "ispA"
source_database: "UniProt"
source_id: "P22939"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ispA b0421 JW0411"
---

# ispA

`protein.P22939`

## Static

- Type: `protein`
- Source: `UniProt:P22939`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

Farnesyl diphosphate synthase (FPP synthase) (EC 2.5.1.10) ((2E,6E)-farnesyl diphosphate synthase) (Geranyltranstransferase) Farnesyl diphosphate synthase can utilize both prenyl (dimethylallyl) and geranyl diphosphates as substrates, generating geranyl and farnesyl diphosphate, respectively. Therefore the enzyme can catalyze two sequential reactions in the polyisoprenoid biosynthetic pathway . Isoprenoid product chain length specificity determinants within IspA were identified by random PCR mutagenesis . Substrate selectivity and stereoselectivity of the enzyme have been investigated . Crystal structures of ternary complexes of the enzyme with substrate(s) or an inhibitor have been solved, revealing the contribution of three Mg2+ ions to substrate binding and catalysis . Even though ispA has been reported to be essential for growth , ispA null mutants are viable, with near-wild type growth yield under anaerobic conditions and a slight reduction in growth yield under aerobic conditions. The mutant contains less than 13% and 18%, respectively, of ubiquinone-8 and menaquinone-8 and 40-70% of the wild-type levels of undecaprenyl phosphate. A low level of geranyl diphosphate synthase activity was detected, which may be due to the activity of other prenyltransferases . A short-chain prenyltransferase activity has been isolated from an ispA mutant strain...

## Biological Role

Catalyzes FPPSYN-RXN (reaction.ecocyc.FPPSYN-RXN), GPPSYN-RXN (reaction.ecocyc.GPPSYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

Farnesyl diphosphate synthase (FPP synthase) (EC 2.5.1.10) ((2E,6E)-farnesyl diphosphate synthase) (Geranyltranstransferase)

## Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.FPPSYN-RXN|reaction.ecocyc.FPPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GPPSYN-RXN|reaction.ecocyc.GPPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0421|gene.b0421]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P22939`
- `KEGG:ecj:JW0411;eco:b0421;ecoc:C3026_02055;`
- `GeneID:93777039;945064;`
- `GO:GO:0004161; GO:0004337; GO:0004659; GO:0005829; GO:0033384; GO:0045337; GO:0046872`
- `EC:2.5.1.10`

## Notes

Farnesyl diphosphate synthase (FPP synthase) (EC 2.5.1.10) ((2E,6E)-farnesyl diphosphate synthase) (Geranyltranstransferase)
