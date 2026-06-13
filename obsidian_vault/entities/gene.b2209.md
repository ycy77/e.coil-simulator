---
entity_id: "gene.b2209"
entity_type: "gene"
name: "eco"
source_database: "NCBI RefSeq"
source_id: "gene-b2209"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2209"
  - "eco"
---

# eco

`gene.b2209`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2209`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eco (gene.b2209) is a gene entity. It encodes eco (protein.P23827). Encoded protein function: FUNCTION: General inhibitor of pancreatic serine proteases: inhibits chymotrypsin, trypsin, elastases, factor X, kallikrein as well as a variety of other proteases. The strength of inhibition does not appear to be correlated with a particular protease specificity. {ECO:0000269|PubMed:35483450}. EcoCyc product frame: EG10255-MONOMER. EcoCyc synonyms: eti. Genomic coordinates: 2303905-2304393. EcoCyc protein note: Ecotin inhibits trypsin and a number of additional heterologous proteases . Some endogenous E. coli proteases are not sensitive to ecotin . Residue Met84 is the reactive site . M84K, M84R, and M84L mutant proteins exhibit altered substrate specificity . The activities of various mutant proteins have been evaluated . Ecotin is implicated in defense from T6SS-mediated killing by TAX-666 . Knockout mutant and crystal structural studies of ecotin interacting with mannan-binding lectin-associated serine proteases (MASPs), components of the lectin pathway of the complement system, revealed ecotin's activity as a microbial defense factor and how binding sites 1 and 2 contribute to ecotin's inhibition of MASP enzymes, thus providing a potential antibiotic target . Ecotin is a homodimer ; each homodimer binds to two protease monomers...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23827|protein.P23827]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=eco; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007297,ECOCYC:EG10255,GeneID:946700`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2303905-2304393:+; feature_type=gene
