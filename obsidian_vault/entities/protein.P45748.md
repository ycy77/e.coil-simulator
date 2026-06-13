---
entity_id: "protein.P45748"
entity_type: "protein"
name: "tsaC"
source_database: "UniProt"
source_id: "P45748"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01852}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tsaC rimN yrdC b3282 JW3243"
---

# tsaC

`protein.P45748`

## Static

- Type: `protein`
- Source: `UniProt:P45748`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01852}.

## Enriched Summary

FUNCTION: Required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in tRNAs that read codons beginning with adenine. Catalyzes the conversion of L-threonine, HCO(3)(-)/CO(2) and ATP to give threonylcarbamoyl-AMP (TC-AMP) as the acyladenylate intermediate, with the release of diphosphate. Is also able to catalyze the reverse reaction in vitro, i.e. the formation of ATP from TC-AMP and PPi. Shows higher affinity for the full-length tRNA(Thr) lacking only the t(6)A37 modification than for its fully modified counterpart. Could also be required for the maturation of 16S rRNA. Binds to double-stranded RNA but does not interact tightly with either of the ribosomal subunits, or the 70S particles. {ECO:0000255|HAMAP-Rule:MF_01852, ECO:0000269|PubMed:15716138, ECO:0000269|PubMed:19287007, ECO:0000269|PubMed:21285948, ECO:0000269|PubMed:22378793, ECO:0000269|PubMed:23072323}. Threonylcarbamoyl-AMP synthase (TsaC) catalyzes the synthesis of threonylcarbamoyl-AMP, an intermediate in the biosynthesis of the threonylcarbamoyladenosine (t6A) modification at position 37 of ANN-decoding tRNAs . Although TsaC (RimN) was initially thought to function as a ribosome maturation factor , new evidence suggested that TsaC is a component of a heteromultimeric complex with threonylcarbamoyltransferase activity...

## Biological Role

Catalyzes RXN-14569 (reaction.ecocyc.RXN-14569).

## Annotation

FUNCTION: Required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in tRNAs that read codons beginning with adenine. Catalyzes the conversion of L-threonine, HCO(3)(-)/CO(2) and ATP to give threonylcarbamoyl-AMP (TC-AMP) as the acyladenylate intermediate, with the release of diphosphate. Is also able to catalyze the reverse reaction in vitro, i.e. the formation of ATP from TC-AMP and PPi. Shows higher affinity for the full-length tRNA(Thr) lacking only the t(6)A37 modification than for its fully modified counterpart. Could also be required for the maturation of 16S rRNA. Binds to double-stranded RNA but does not interact tightly with either of the ribosomal subunits, or the 70S particles. {ECO:0000255|HAMAP-Rule:MF_01852, ECO:0000269|PubMed:15716138, ECO:0000269|PubMed:19287007, ECO:0000269|PubMed:21285948, ECO:0000269|PubMed:22378793, ECO:0000269|PubMed:23072323}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-14569|reaction.ecocyc.RXN-14569]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3282|gene.b3282]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45748`
- `KEGG:ecj:JW3243;eco:b3282;ecoc:C3026_17850;`
- `GeneID:947783;`
- `GO:GO:0000049; GO:0002949; GO:0003725; GO:0005524; GO:0005737; GO:0005829; GO:0006364; GO:0006450; GO:0016779; GO:0061710`
- `EC:2.7.7.87`

## Notes

Threonylcarbamoyl-AMP synthase (TC-AMP synthase) (EC 2.7.7.87) (L-threonylcarbamoyladenylate synthase) (Ribosome maturation factor TsaC) (t(6)A37 threonylcarbamoyladenosine biosynthesis protein TsaC) (tRNA threonylcarbamoyladenosine biosynthesis protein TsaC)
