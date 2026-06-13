---
entity_id: "protein.P0AEI1"
entity_type: "protein"
name: "miaB"
source_database: "UniProt"
source_id: "P0AEI1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01864}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "miaB yleA b0661 JW0658"
---

# miaB

`protein.P0AEI1`

## Static

- Type: `protein`
- Source: `UniProt:P0AEI1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01864}.

## Enriched Summary

FUNCTION: Catalyzes the methylthiolation of N6-(dimethylallyl)adenosine (i(6)A), leading to the formation of 2-methylthio-N6-(dimethylallyl)adenosine (ms(2)i(6)A) at position 37 in tRNAs that read codons beginning with uridine. {ECO:0000255|HAMAP-Rule:MF_01864, ECO:0000269|PubMed:10572129}. MiaB is an isopentenyl-adenosine tRNA methylthiolase. Most E. coli tRNAs that read codons starting with U contain the modified base 2-methylthio-N6-isopentenyladenosine-37 (ms2i6A37) . MiaB is required for both sulfur insertion and methylation at carbon 2 of N6-isopentenyladenosine-37 in tRNA, yielding the final modified ms2i6A37 tRNA . MiaB is a member of the Radical SAM protein superfamily and was originally reported to bind two 4Fe-4S clusters . From studies in E. coli strain C6, the reaction is thought to take place in two steps: thiolation followed by methylation . It is thought that the G7511 "YgfZ protein" is involved in the repair/exchange of the spent cluster of both MiaB and the homologous enzyme G6435 RimO . MiaB interacts with CPLX0-7682 "NfuA" and EG12181-MONOMER "GrxD". NfuA, but not GrxD, can transfer a 4Fe-4S cluster to apo-MiaB in vitro, and both proteins affect MiaB activity in vivo . A miaB mutant accumulates under-modified i6A tRNA . However, unlike mutants in the associated gene miaA, miaB mutants do not have a mutator phenotype or a drop in tetracycline resistance...

## Biological Role

Catalyzes RXN0-5063 (reaction.ecocyc.RXN0-5063). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

FUNCTION: Catalyzes the methylthiolation of N6-(dimethylallyl)adenosine (i(6)A), leading to the formation of 2-methylthio-N6-(dimethylallyl)adenosine (ms(2)i(6)A) at position 37 in tRNAs that read codons beginning with uridine. {ECO:0000255|HAMAP-Rule:MF_01864, ECO:0000269|PubMed:10572129}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5063|reaction.ecocyc.RXN0-5063]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0661|gene.b0661]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEI1`
- `KEGG:ecj:JW0658;eco:b0661;ecoc:C3026_03305;`
- `GeneID:86863171;945260;`
- `GO:GO:0005829; GO:0030488; GO:0035597; GO:0035600; GO:0046872; GO:0051539`
- `EC:2.8.4.3`

## Notes

tRNA-2-methylthio-N(6)-dimethylallyladenosine synthase (EC 2.8.4.3) ((Dimethylallyl)adenosine tRNA methylthiotransferase MiaB) (tRNA-i(6)A37 methylthiotransferase)
