---
entity_id: "protein.P0A6M2"
entity_type: "protein"
name: "dsbB"
source_database: "UniProt"
source_id: "P0A6M2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:7957076, ECO:0000269|PubMed:8430071}; Multi-pass membrane protein {ECO:0000269|PubMed:7957076, ECO:0000269|PubMed:8430071}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dsbB roxB ycgA b1185 JW5182"
---

# dsbB

`protein.P0A6M2`

## Static

- Type: `protein`
- Source: `UniProt:P0A6M2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:7957076, ECO:0000269|PubMed:8430071}; Multi-pass membrane protein {ECO:0000269|PubMed:7957076, ECO:0000269|PubMed:8430071}.

## Enriched Summary

FUNCTION: Required for disulfide bond formation in some periplasmic proteins such as PhoA or OmpA. Acts by oxidizing the DsbA protein. PhoP-regulated transcription is redox-sensitive, being activated when the periplasm becomes more reducing (deletion of dsbA/dsbB, treatment with dithiothreitol). MgrB acts between DsbA/DsbB and PhoP/PhoQ in this pathway. {ECO:0000269|PubMed:22267510, ECO:0000269|PubMed:7688471, ECO:0000269|PubMed:8430071}. DsbB is a protein thiol:quinone oxidoreductase that functions within a pathway for protein disulfide bond formation; DsbB catalyses the oxidation of DsbA via the reduction of membrane quinones; DsbB, in conjunction with membrane quinones generates disulfide bonds de novo and is considered to be a disulfide bond manufacturer within E. coli K-12 (reviewed in ). DsbB null mutants (dsbB::kan5) synthesize OmpA and β-lactamase proteins that are deficient in disulfide bonds and this defect can be rescued by supplementation with cystine or oxidized glutathione; DsbA is present in the fully reduced state in DsbB null mutants (see also ). dsb mutant strains (ΔdsbB, ΔdsbA and ΔdsbAB) have unimpaired growth under aerobic conditions but show a severe growth defect under anaerobic conditions which can be suppressed by supplementation with cystine...

## Biological Role

Catalyzes RXN-19988 (reaction.ecocyc.RXN-19988), RXN-19998 (reaction.ecocyc.RXN-19998).

## Annotation

FUNCTION: Required for disulfide bond formation in some periplasmic proteins such as PhoA or OmpA. Acts by oxidizing the DsbA protein. PhoP-regulated transcription is redox-sensitive, being activated when the periplasm becomes more reducing (deletion of dsbA/dsbB, treatment with dithiothreitol). MgrB acts between DsbA/DsbB and PhoP/PhoQ in this pathway. {ECO:0000269|PubMed:22267510, ECO:0000269|PubMed:7688471, ECO:0000269|PubMed:8430071}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-19988|reaction.ecocyc.RXN-19988]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-19998|reaction.ecocyc.RXN-19998]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1185|gene.b1185]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6M2`
- `KEGG:ecj:JW5182;eco:b1185;ecoc:C3026_06980;`
- `GeneID:75203298;946344;`
- `GO:GO:0005886; GO:0006457; GO:0009055; GO:0009408; GO:0015035; GO:0016672; GO:0048039`

## Notes

Disulfide bond formation protein B (Disulfide oxidoreductase)
