---
entity_id: "gene.b2743"
entity_type: "gene"
name: "pcm"
source_database: "NCBI RefSeq"
source_id: "gene-b2743"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2743"
  - "pcm"
---

# pcm

`gene.b2743`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2743`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pcm (gene.b2743) is a gene entity. It encodes pcm (protein.P0A7A5). Encoded protein function: FUNCTION: Catalyzes the methyl esterification of L-isoaspartyl residues in peptides and proteins that result from spontaneous decomposition of normal L-aspartyl and L-asparaginyl residues. It plays a role in the repair and/or degradation of damaged proteins. This enzyme does not act on D-aspartyl residues. EcoCyc product frame: EG10689-MONOMER. Genomic coordinates: 2868893-2869519. EcoCyc protein note: L-isoaspartate protein carboxylmethyltransferase (PIMT) transfers a methyl group from S-adenosylmethionine (SAM) to the free carboxyl group of D-aspartyl and L-isoaspartyl residues within polypeptides. The enzyme may therefore serve to repair abnormal L-isoaspartyl residues that arise spontaneously from aspartyl and asparaginyl residues in proteins. PIMT enhances survival of E. coli under conditions of environmental stress in late stationary phase and oxidative stress at alkaline pH . PIMT is monomeric in solution. A crystal structure of PIMT was solved at 1.8 Å resolution . Enzymes containing mutations in glutamate residues that were predicted to be involved in SAM binding retained the ability to bind SAM, but altered the kinetic properties of the enzyme . Overexpression of pcm leads to increased tolerance for thermal stress, likely due to induction of the misfolded protein response...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7A5|protein.P0A7A5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pcm; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009006,ECOCYC:EG10689,GeneID:944923`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2868893-2869519:-; feature_type=gene
