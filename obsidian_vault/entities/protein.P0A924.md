---
entity_id: "protein.P0A924"
entity_type: "protein"
name: "pgpB"
source_database: "UniProt"
source_id: "P0A924"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}. Cell outer membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pgpB b1278 JW1270"
---

# pgpB

`protein.P0A924`

## Static

- Type: `protein`
- Source: `UniProt:P0A924`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}. Cell outer membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Catalyzes the dephosphorylation of diacylglycerol diphosphate (DGPP) to phosphatidate (PA) and the subsequent dephosphorylation of PA to diacylglycerol (DAG). Also has undecaprenyl pyrophosphate phosphatase activity, required for the biosynthesis of the lipid carrier undecaprenyl phosphate. Can also use lysophosphatidic acid (LPA) and phosphatidylglycerophosphate as substrates. The pattern of activities varies according to subcellular location, PGP phosphatase activity is higher in the cytoplasmic membrane, whereas PA and LPA phosphatase activities are higher in the outer membrane. Activity is independent of a divalent cation ion and insensitive to inhibition by N-ethylmaleimide. {ECO:0000269|PubMed:15778224, ECO:0000269|PubMed:18411271, ECO:0000269|PubMed:21148555, ECO:0000269|PubMed:8940025}. E. coli contains three phosphatidylglycerophosphatases - EG10704 "PgpA", PgpB and EG11371 "PgpC" - which catalyse the dephosphorylation of phosphatidylglycerol phosphate (PGP) to phosphatidylglycerol (PG), an essential phospholipid of the inner and outer membrane in E. coli. PgpA and PgpC appear to be specific for PGP whereas PgpB is a multifunctional enzyme that is also active on undecaprenyl diphosphate (C55PP), phosphatidicic acid and lysophosphatidic acid . The main physiological activity of PgpB may be its diacylglycerol pyrophosphate (DGPP) phosphatase activity...

## Biological Role

Catalyzes 1-alkyl-2-acyl-sn-glycero-3-phosphate phosphohydrolase (reaction.R04162), PGPPHOSPHA-RXN (reaction.ecocyc.PGPPHOSPHA-RXN), RXN-11277 (reaction.ecocyc.RXN-11277), UNDECAPRENYL-DIPHOSPHATASE-RXN (reaction.ecocyc.UNDECAPRENYL-DIPHOSPHATASE-RXN).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the dephosphorylation of diacylglycerol diphosphate (DGPP) to phosphatidate (PA) and the subsequent dephosphorylation of PA to diacylglycerol (DAG). Also has undecaprenyl pyrophosphate phosphatase activity, required for the biosynthesis of the lipid carrier undecaprenyl phosphate. Can also use lysophosphatidic acid (LPA) and phosphatidylglycerophosphate as substrates. The pattern of activities varies according to subcellular location, PGP phosphatase activity is higher in the cytoplasmic membrane, whereas PA and LPA phosphatase activities are higher in the outer membrane. Activity is independent of a divalent cation ion and insensitive to inhibition by N-ethylmaleimide. {ECO:0000269|PubMed:15778224, ECO:0000269|PubMed:18411271, ECO:0000269|PubMed:21148555, ECO:0000269|PubMed:8940025}.

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R04162|reaction.R04162]] `KEGG` `database` - via EC:3.1.3.4
- `catalyzes` --> [[reaction.ecocyc.PGPPHOSPHA-RXN|reaction.ecocyc.PGPPHOSPHA-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-11277|reaction.ecocyc.RXN-11277]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.UNDECAPRENYL-DIPHOSPHATASE-RXN|reaction.ecocyc.UNDECAPRENYL-DIPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1278|gene.b1278]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A924`
- `KEGG:ecj:JW1270;eco:b1278;ecoc:C3026_07505;`
- `GeneID:75171395;75203391;945863;`
- `GO:GO:0000810; GO:0005886; GO:0006655; GO:0008195; GO:0008962; GO:0009252; GO:0009279; GO:0009395; GO:0046474; GO:0050380`
- `EC:3.1.3.27; 3.1.3.4; 3.6.1.27; 3.6.1.75`

## Notes

Phosphatidylglycerophosphatase B (EC 3.1.3.27) (Diacylglycerol pyrophosphate phosphatase) (DGPP phosphatase) (EC 3.6.1.75) (Phosphatidate phosphatase) (EC 3.1.3.4) (Undecaprenyl pyrophosphate phosphatase) (EC 3.6.1.27) (Undecaprenyl-diphosphatase)
