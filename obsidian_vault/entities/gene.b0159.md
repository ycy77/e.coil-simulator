---
entity_id: "gene.b0159"
entity_type: "gene"
name: "mtn"
source_database: "NCBI RefSeq"
source_id: "gene-b0159"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0159"
  - "mtn"
---

# mtn

`gene.b0159`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0159`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mtn (gene.b0159) is a gene entity. It encodes mtnN (protein.P0AF12). Encoded protein function: FUNCTION: Catalyzes the irreversible cleavage of the glycosidic bond in both 5'-methylthioadenosine (MTA) and S-adenosylhomocysteine (SAH/AdoHcy) to adenine and the corresponding thioribose, 5'-methylthioribose and S-ribosylhomocysteine, respectively (PubMed:16101288, PubMed:3911944). Also cleaves 5'-deoxyadenosine, a toxic by-product of radical S-adenosylmethionine (SAM) enzymes, into 5-deoxyribose and adenine. Thus, is required for in vivo function of the radical SAM enzymes biotin synthase and lipoic acid synthase, that are inhibited by 5'-deoxyadenosine accumulation (PubMed:15911379). Can also use 5'-isobutylthioadenosine, 5'-n-butylthioadenosine, S-adenosyl-D-homocysteine, decarboxylated adenosylhomocysteine, deaminated adenosylhomocysteine and S-2-aza-adenosylhomocysteine as substrates in vitro (PubMed:3911944). {ECO:0000269|PubMed:15911379, ECO:0000269|PubMed:16101288, ECO:0000269|PubMed:3911944}. EcoCyc product frame: EG11090-MONOMER. EcoCyc synonyms: pfs, yadA, mtnN. Genomic coordinates: 178455-179153.

## Biological Role

Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), rpoD (protein.P00579), rpoS (protein.P13445).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF12|protein.P0AF12]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mtn; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=mtn; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000545,ECOCYC:EG11090,GeneID:948542`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:178455-179153:-; feature_type=gene
