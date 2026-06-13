---
entity_id: "gene.b0907"
entity_type: "gene"
name: "serC"
source_database: "NCBI RefSeq"
source_id: "gene-b0907"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0907"
  - "serC"
---

# serC

`gene.b0907`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0907`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

serC (gene.b0907) is a gene entity. It encodes serC (protein.P23721). Encoded protein function: FUNCTION: Catalyzes the reversible conversion of 3-phosphohydroxypyruvate to phosphoserine and of 3-hydroxy-2-oxo-4-phosphonooxybutanoate to phosphohydroxythreonine. Is involved in both pyridoxine and serine biosynthesis. {ECO:0000269|PubMed:2121717, ECO:0000269|PubMed:8706854}. EcoCyc product frame: PSERTRANSAM-MONOMER. EcoCyc synonyms: pdxC, pdxF. Genomic coordinates: 957653-958741. EcoCyc protein note: The serC-encoded enzyme, phosphoserine/phosphohydroxythreonine aminotransferase, functions in the biosythesis of both serine and pyridoxine, by using different substrates . Pyridoxal 5'-phosphate is a cofactor for both enzyme activities, suggesting that it can act in an autocatalytic fashion, stimulating its own biosynthesis . The redundancy and promiscuity among aminotransferase enzymes has been investigated. stated that no activity could be observed with non-phosphorylated substrates; however, was able to use 3-hydroxypyruvate as the substrate for an assay of SerC enzymatic activity. In addition, genetic experiments showed that SerC is a minor alanine transaminase...

## Biological Role

Repressed by lrp (protein.P0ACJ0), crp (protein.P0ACJ8). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23721|protein.P23721]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=serC; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=serC; function=-+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `C` - regulator=Lrp; target=serC; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=serC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003093,ECOCYC:EG10946,GeneID:945527`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:957653-958741:+; feature_type=gene
