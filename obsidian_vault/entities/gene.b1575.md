---
entity_id: "gene.b1575"
entity_type: "gene"
name: "dicB"
source_database: "NCBI RefSeq"
source_id: "gene-b1575"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1575"
  - "dicB"
---

# dicB

`gene.b1575`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1575`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dicB (gene.b1575) is a gene entity. It encodes dicB (protein.P09557). Encoded protein function: FUNCTION: Involved in cell division inhibition; this function can be repressed by DicA and DicC proteins as well as antitoxin CbeA (yeeU). {ECO:0000269|PubMed:22515815}. EcoCyc product frame: EG10227-MONOMER. EcoCyc synonyms: ftsT. Genomic coordinates: 1649609-1649797. EcoCyc protein note: DicB is a small protein encoded on the Qin prophage and is involved in the regulation of cell division . The N terminus of DicB is essential for its function as an inhibitor of cell division . EG10596-MONOMER MinC is involved in both the DicB pathway of inhibition of cell division and in the MinC-MinD inhibition pathway . DicB interacts with the C-terminal domain of MinC; the complex then interacts with the septal ring, where it inhibits stable FtsZ ring formation . Targeting of DicB-MinC to the septal ring requires ZipA . Inducing expression of the "dicBF operon" using a Plac promoter in place of the native promoter upstream of ydfA confers substantial resistance to infection by λvir. This phenotype is mostly due to expression of DicB, which inhibits injection of phage DNA through the inner membrane proteins ManYZ. The DicB expression phenotypes require the interaction of DicB with MinC . A dicB mutation suppresses the heat sensitivity of a dicA1 recA double mutant...

## Biological Role

Repressed by yjdC (protein.P0ACU7).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09557|protein.P09557]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACU7|protein.P0ACU7]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005260,ECOCYC:EG10227,GeneID:946110`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1649609-1649797:+; feature_type=gene
