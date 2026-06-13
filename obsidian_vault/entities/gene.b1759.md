---
entity_id: "gene.b1759"
entity_type: "gene"
name: "nudG"
source_database: "NCBI RefSeq"
source_id: "gene-b1759"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1759"
  - "nudG"
---

# nudG

`gene.b1759`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1759`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nudG (gene.b1759) is a gene entity. It encodes nudG (protein.P77788). Encoded protein function: FUNCTION: Hydrolase with a preference for pyrimidine substrates. Has high activity with 5-methyl-dCTP, and much lower activity with CTP, dCTP, 5-hydroxy-dCTP, 2-hydroxy-dATP and 8-hydroxy-dGTP. {ECO:0000269|PubMed:11053429, ECO:0000269|PubMed:12509230, ECO:0000269|PubMed:15823026}. EcoCyc product frame: G6954-MONOMER. EcoCyc synonyms: ynjG, orf135. Genomic coordinates: 1841490-1841897. EcoCyc protein note: NudG is a member of the Nudix hydrolase family and shows high specificity for hydrolysis of pyrimidine (deoxy)nucleoside triphosphates . The enzyme hydrolyzes oxidized nucleotides and is therefore expected to function in DNA damage avoidance . Its preferred substrate appears to be 5-hydroxy-CTP . A solution structure of NudG has been obtained, enabling identification of the substrate binding pocket . A nudG deletion strain exhibits a 2-3-fold elevated rate of HYDROGEN-PEROXIDE-induced mutations, while overexpression of nudG suppressed mutations . Site-directed mutagenesis of various conserved amino acid residues has been performed , and residues involved in substrate binding have been identified .

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77788|protein.P77788]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=nudG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005855,ECOCYC:G6954,GeneID:946277`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1841490-1841897:+; feature_type=gene
