---
entity_id: "protein.P0AFB8"
entity_type: "protein"
name: "glnG"
source_database: "UniProt"
source_id: "P0AFB8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glnG glnT ntrC b3868 JW3839"
---

# glnG

`protein.P0AFB8`

## Static

- Type: `protein`
- Source: `UniProt:P0AFB8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system NtrB/NtrC, which controls expression of the nitrogen-regulated (ntr) genes in response to nitrogen limitation. Phosphorylated NtrC binds directly to DNA and stimulates the formation of open promoter-sigma54-RNA polymerase complexes (PubMed:1350679, PubMed:2574599, PubMed:2874557, PubMed:3304660). Activates transcription of many genes and operons whose products minimize the slowing of growth under nitrogen-limiting conditions, including genes coding for glutamine synthetase (glnA), transporters, amino acid permeases and catabolic enzymes (PubMed:11121068). {ECO:0000269|PubMed:11121068, ECO:0000269|PubMed:1350679, ECO:0000269|PubMed:2574599, ECO:0000269|PubMed:2874557, ECO:0000269|PubMed:3304660}.

## Biological Role

Component of NtrC phosphorylated dimer (complex.ecocyc.CPLX0-8566), DNA-binding transcriptional dual regulator NtrC (complex.ecocyc.GLNG-CPLX), DNA-binding transcriptional dual regulator NtrC-phosphorylated (complex.ecocyc.PROTEIN-NRIP).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system NtrB/NtrC, which controls expression of the nitrogen-regulated (ntr) genes in response to nitrogen limitation. Phosphorylated NtrC binds directly to DNA and stimulates the formation of open promoter-sigma54-RNA polymerase complexes (PubMed:1350679, PubMed:2574599, PubMed:2874557, PubMed:3304660). Activates transcription of many genes and operons whose products minimize the slowing of growth under nitrogen-limiting conditions, including genes coding for glutamine synthetase (glnA), transporters, amino acid permeases and catabolic enzymes (PubMed:11121068). {ECO:0000269|PubMed:11121068, ECO:0000269|PubMed:1350679, ECO:0000269|PubMed:2574599, ECO:0000269|PubMed:2874557, ECO:0000269|PubMed:3304660}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (46)

- `activates` --> [[gene.b0809|gene.b0809]] `RegulonDB` `S` - regulator=NtrC; target=glnQ; function=-+
- `activates` --> [[gene.b0810|gene.b0810]] `RegulonDB` `S` - regulator=NtrC; target=glnP; function=-+
- `activates` --> [[gene.b0811|gene.b0811]] `RegulonDB` `S` - regulator=NtrC; target=glnH; function=-+
- `activates` --> [[gene.b1006|gene.b1006]] `RegulonDB` `S` - regulator=NtrC; target=rutG; function=+
- `activates` --> [[gene.b1007|gene.b1007]] `RegulonDB` `S` - regulator=NtrC; target=rutF; function=+
- `activates` --> [[gene.b1008|gene.b1008]] `RegulonDB` `S` - regulator=NtrC; target=rutE; function=+
- `activates` --> [[gene.b1009|gene.b1009]] `RegulonDB` `S` - regulator=NtrC; target=rutD; function=+
- `activates` --> [[gene.b1010|gene.b1010]] `RegulonDB` `S` - regulator=NtrC; target=rutC; function=+
- `activates` --> [[gene.b1011|gene.b1011]] `RegulonDB` `S` - regulator=NtrC; target=rutB; function=+
- `activates` --> [[gene.b1012|gene.b1012]] `RegulonDB` `S` - regulator=NtrC; target=rutA; function=+
- `activates` --> [[gene.b1744|gene.b1744]] `RegulonDB` `S` - regulator=NtrC; target=astE; function=+
- `activates` --> [[gene.b1745|gene.b1745]] `RegulonDB` `S` - regulator=NtrC; target=astB; function=+
- `activates` --> [[gene.b1746|gene.b1746]] `RegulonDB` `S` - regulator=NtrC; target=astD; function=+
- `activates` --> [[gene.b1747|gene.b1747]] `RegulonDB` `S` - regulator=NtrC; target=astA; function=+
- `activates` --> [[gene.b1748|gene.b1748]] `RegulonDB` `S` - regulator=NtrC; target=astC; function=+
- `activates` --> [[gene.b1988|gene.b1988]] `RegulonDB` `S` - regulator=NtrC; target=nac; function=+
- `activates` --> [[gene.b2306|gene.b2306]] `RegulonDB` `S` - regulator=NtrC; target=hisP; function=+
- `activates` --> [[gene.b2307|gene.b2307]] `RegulonDB` `S` - regulator=NtrC; target=hisM; function=+
- `activates` --> [[gene.b2308|gene.b2308]] `RegulonDB` `S` - regulator=NtrC; target=hisQ; function=+
- `activates` --> [[gene.b2309|gene.b2309]] `RegulonDB` `S` - regulator=NtrC; target=hisJ; function=+
- `activates` --> [[gene.b2310|gene.b2310]] `RegulonDB` `S` - regulator=NtrC; target=argT; function=+
- `activates` --> [[gene.b2570|gene.b2570]] `RegulonDB` `S` - regulator=NtrC; target=rseC; function=+
- `activates` --> [[gene.b2571|gene.b2571]] `RegulonDB` `S` - regulator=NtrC; target=rseB; function=+
- `activates` --> [[gene.b2572|gene.b2572]] `RegulonDB` `S` - regulator=NtrC; target=rseA; function=+
- `activates` --> [[gene.b2573|gene.b2573]] `RegulonDB` `S` - regulator=NtrC; target=rpoE; function=+
- `activates` --> [[gene.b2784|gene.b2784]] `RegulonDB` `S` - regulator=NtrC; target=relA; function=+
- `activates` --> [[gene.b3073|gene.b3073]] `RegulonDB` `S` - regulator=NtrC; target=patA; function=+
- `activates` --> [[gene.b3269|gene.b3269]] `RegulonDB` `S` - regulator=NtrC; target=yhdX; function=+
- `activates` --> [[gene.b3270|gene.b3270]] `RegulonDB` `S` - regulator=NtrC; target=yhdY; function=+
- `activates` --> [[gene.b3271|gene.b3271]] `RegulonDB` `S` - regulator=NtrC; target=yhdZ; function=+
- `activates` --> [[gene.b3868|gene.b3868]] `RegulonDB` `S` - regulator=NtrC; target=glnG; function=-+
- `activates` --> [[gene.b3869|gene.b3869]] `RegulonDB` `S` - regulator=NtrC; target=glnL; function=-+
- `activates` --> [[gene.b3870|gene.b3870]] `RegulonDB` `C` - regulator=NtrC; target=glnA; function=-+
- `activates` --> [[gene.b4725|gene.b4725]] `RegulonDB` `S` - regulator=NtrC; target=rseD; function=+
- `activates` --> [[gene.b4836|gene.b4836]] `RegulonDB` `C` - regulator=NtrC; target=glnZ; function=-+
- `is_component_of` --> [[complex.ecocyc.CPLX0-8566|complex.ecocyc.CPLX0-8566]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.GLNG-CPLX|complex.ecocyc.GLNG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.PROTEIN-NRIP|complex.ecocyc.PROTEIN-NRIP]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6
- `represses` --> [[gene.b0809|gene.b0809]] `RegulonDB` `S` - regulator=NtrC; target=glnQ; function=-+
- `represses` --> [[gene.b0810|gene.b0810]] `RegulonDB` `S` - regulator=NtrC; target=glnP; function=-+
- `represses` --> [[gene.b0811|gene.b0811]] `RegulonDB` `S` - regulator=NtrC; target=glnH; function=-+
- `represses` --> [[gene.b1781|gene.b1781]] `RegulonDB` `S` - regulator=NtrC; target=yeaE; function=-
- `represses` --> [[gene.b3868|gene.b3868]] `RegulonDB` `S` - regulator=NtrC; target=glnG; function=-+
- `represses` --> [[gene.b3869|gene.b3869]] `RegulonDB` `S` - regulator=NtrC; target=glnL; function=-+
- `represses` --> [[gene.b3870|gene.b3870]] `RegulonDB` `C` - regulator=NtrC; target=glnA; function=-+
- `represses` --> [[gene.b4836|gene.b4836]] `RegulonDB` `C` - regulator=NtrC; target=glnZ; function=-+

## Incoming Edges (1)

- `encodes` <-- [[gene.b3868|gene.b3868]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFB8`
- `KEGG:ecj:JW3839;eco:b3868;ecoc:C3026_20910;`
- `GeneID:75174103;948361;`
- `GO:GO:0000156; GO:0000987; GO:0001216; GO:0005524; GO:0005829; GO:0006808; GO:0032993; GO:0045893`

## Notes

DNA-binding transcriptional regulator NtrC (Nitrogen regulation protein NR(I)) (Nitrogen regulator I) (NRI)
