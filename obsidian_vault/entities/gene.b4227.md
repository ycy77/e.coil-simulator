---
entity_id: "gene.b4227"
entity_type: "gene"
name: "ytfQ"
source_database: "NCBI RefSeq"
source_id: "gene-b4227"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4227"
  - "ytfQ"
---

# ytfQ

`gene.b4227`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4227`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ytfQ (gene.b4227) is a gene entity. It encodes ytfQ (protein.P39325). Encoded protein function: FUNCTION: Part of the ABC transporter complex YtfQRT-YjfF involved in galactofuranose transport (Probable). Binds to both alpha- and beta-galactofuranose (PubMed:19744923). {ECO:0000269|PubMed:19744923, ECO:0000305|PubMed:19744923}. EcoCyc product frame: YTFQ-MONOMER. Genomic coordinates: 4449962-4450918. EcoCyc protein note: YtfQ is the periplasmic binding component of a galactofuranose ABC transporter. Purified YtfQ binds galactose with a Kd of 1.7μM and arabinose with a Kd of 1.3μM; YtfQ exhibits selective binding of galactofuranose over galactopyranose; the inferred affinity of YtfQ for galactofuranose is 0.13μM; YtfQ is able to recognise both α and β forms of galactofuranose; YtfQ does not bind glucose . The crystal structure of YtfQ with a single molecule of galactofuranose in its ligand binding pocket has been resolved at 1.2Å. The binding protein has two α/β domains linked by a hinge region; galactofuranose binds in a cleft between the two domains and is totally buried within the protein; a disulfide bond is present between cysteine residues 129 and 193 . YtfQ is upregulated in fed-batch phase (compared to exponential phase) during glucose-limited fermentation .

## Biological Role

Repressed by araC (protein.P0A9E0).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39325|protein.P39325]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `S` - regulator=AraC; target=ytfQ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013829,ECOCYC:EG12517,GeneID:948746`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4449962-4450918:+; feature_type=gene
