---
entity_id: "protein.P21499"
entity_type: "protein"
name: "rnr"
source_database: "UniProt"
source_id: "P21499"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rnr vacB yjeC b4179 JW5741"
---

# rnr

`protein.P21499`

## Static

- Type: `protein`
- Source: `UniProt:P21499`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: 3'-5' exoribonuclease that releases 5'-nucleoside monophosphates and is involved in maturation of structured RNAs (rRNAs, tRNAs and SsrA/tmRNA). In stationary phase, involved in the post-transcriptional regulation of ompA mRNA stability. Shortens RNA processively to di- and trinucleotides. In vitro, exhibits helicase activity, which is independent of its RNase activity. RNases 2 and R (rnb and this entry) contribute to rRNA degradation during starvation, while RNase R and PNPase (this entry and pnp) are the major contributors to quality control of rRNA during steady state growth (PubMed:21135037). Required for the expression of virulence genes in enteroinvasive strains of E.coli. {ECO:0000269|PubMed:11948193, ECO:0000269|PubMed:14622421, ECO:0000269|PubMed:16556233, ECO:0000269|PubMed:20023028, ECO:0000269|PubMed:21135037}. RNase R is a ribonuclease that has been implicated in rRNA maturation, mRNA degradation during stationary phase, degradation of polyadenylated mRNAs, and tmRNA-mediated degradation of non-stop mRNAs. RNase R is a processive hydrolytic 3' to 5' exoribonuclease that releases 5'-nucleoside monophosphates, producing limit end products of di- and trinucleotides. Although it can cleave several RNA substrates, it shows greatest activity toward rRNA...

## Biological Role

Catalyzes RXN0-7023 (reaction.ecocyc.RXN0-7023). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

FUNCTION: 3'-5' exoribonuclease that releases 5'-nucleoside monophosphates and is involved in maturation of structured RNAs (rRNAs, tRNAs and SsrA/tmRNA). In stationary phase, involved in the post-transcriptional regulation of ompA mRNA stability. Shortens RNA processively to di- and trinucleotides. In vitro, exhibits helicase activity, which is independent of its RNase activity. RNases 2 and R (rnb and this entry) contribute to rRNA degradation during starvation, while RNase R and PNPase (this entry and pnp) are the major contributors to quality control of rRNA during steady state growth (PubMed:21135037). Required for the expression of virulence genes in enteroinvasive strains of E.coli. {ECO:0000269|PubMed:11948193, ECO:0000269|PubMed:14622421, ECO:0000269|PubMed:16556233, ECO:0000269|PubMed:20023028, ECO:0000269|PubMed:21135037}.

## Pathways

- `eco03018` RNA degradation (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7023|reaction.ecocyc.RXN0-7023]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4179|gene.b4179]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21499`
- `KEGG:ecj:JW5741;eco:b4179;ecoc:C3026_22580;`
- `GeneID:948692;`
- `GO:GO:0000175; GO:0003723; GO:0004540; GO:0005829; GO:0006397; GO:0006402; GO:0006950; GO:0008859; GO:0009409; GO:0016896; GO:0034458`
- `EC:3.1.13.1`

## Notes

Ribonuclease R (RNase R) (EC 3.1.13.1) (Protein VacB)
