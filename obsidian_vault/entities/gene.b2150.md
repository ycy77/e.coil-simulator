---
entity_id: "gene.b2150"
entity_type: "gene"
name: "mglB"
source_database: "NCBI RefSeq"
source_id: "gene-b2150"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2150"
  - "mglB"
---

# mglB

`gene.b2150`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2150`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mglB (gene.b2150) is a gene entity. It encodes mglB (protein.P0AEE5). Encoded protein function: FUNCTION: Part of the ABC transporter complex MglABC involved in galactose/methyl galactoside import (Probable). In addition, binds D-galactose and D-glucose and plays a role in the chemotaxis towards these two sugars by interacting with the Trg chemoreceptor (PubMed:3057628, PubMed:4927373). Chemotaxis requires MglB, but not MglA or MglC (PubMed:6294056). {ECO:0000269|PubMed:3057628, ECO:0000269|PubMed:4927373, ECO:0000269|PubMed:6294056, ECO:0000305|PubMed:1719366, ECO:0000305|PubMed:6294056}. EcoCyc product frame: MGLB-MONOMER. Genomic coordinates: 2239350-2240348. EcoCyc protein note: MglB is the periplasmic binding protein of a D-galactose / methyl-D-galactoside ABC transport system; ligand bound MglB also interacts with the EG11018 "Trg" sensory protein to mediate taxis to galactose and glucose. mglB mutants are defective in both galactose transport and galactose taxis . mglB mutants are unable to accumulate labeled methyl-β-D-galactopyranoside . mglB+ plasmids synthesize both the precursor and the mature form of galactose binding protein in minicells; chemotaxis towards galactose requires MglB but not MglA or MglC . MglB (purified from E. coli W3092) has a single binding site and binds galactose and glucose with µM affinity...

## Biological Role

Repressed by nac (protein.Q47005). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEE5|protein.P0AEE5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=mglB; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=mglB; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=mglB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007108,ECOCYC:EG10593,GeneID:949041`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2239350-2240348:-; feature_type=gene
