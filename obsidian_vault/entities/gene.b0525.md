---
entity_id: "gene.b0525"
entity_type: "gene"
name: "ppiB"
source_database: "NCBI RefSeq"
source_id: "gene-b0525"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0525"
  - "ppiB"
---

# ppiB

`gene.b0525`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0525`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ppiB (gene.b0525) is a gene entity. It encodes ppiB (protein.P23869). Encoded protein function: FUNCTION: PPIases accelerate the folding of proteins. It catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides. {ECO:0000269|PubMed:1606970, ECO:0000269|PubMed:2007139}. EcoCyc product frame: EG10758-MONOMER. Genomic coordinates: 553943-554437. EcoCyc protein note: PpiB is a single-domain peptidyl-prolyl cis-trans-isomerase (PPIase) that is the main contributor to PPIase activity in the cytoplasm . PPIases catalyze the conformational isomerization of prolyl residues in peptides; cis-trans isomerization of prolyl peptide bonds is a slow step in protein folding. PpiB was shown to improve the efficiency of bovine protein disulfide isomerase as a catalyst of oxidative protein folding and to catalyze the refolding of denatured type III collagen . Unlike the eukaryotic cyclophilins, PpiB activity is only inhibited by high concentrations of cyclosporin A or FK506 . Putative substrates of PpiB activity, including DnaK, PflB and Pta, have been identified . Consistent with its role as the major cytoplasmic PPIase, PpiB has a large number of substrates . Crystal structures in two different conformations and a solution structure of PpiB have been determined. Refolding kinetics of the protein have been studied...

## Biological Role

Repressed by nac (protein.Q47005). Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23869|protein.P23869]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ppiB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ppiB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001806,ECOCYC:EG10758,GeneID:949038`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:553943-554437:-; feature_type=gene
