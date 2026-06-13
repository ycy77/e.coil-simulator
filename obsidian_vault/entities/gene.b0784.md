---
entity_id: "gene.b0784"
entity_type: "gene"
name: "moaD"
source_database: "NCBI RefSeq"
source_id: "gene-b0784"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0784"
  - "moaD"
---

# moaD

`gene.b0784`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0784`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

moaD (gene.b0784) is a gene entity. It encodes moaD (protein.P30748). Encoded protein function: FUNCTION: Involved in sulfur transfer in the conversion of molybdopterin precursor Z to molybdopterin. {ECO:0000269|PubMed:17223713}. EcoCyc product frame: EG11597-MONOMER. EcoCyc synonyms: chlA4, chlM. Genomic coordinates: 819048-819293. EcoCyc protein note: Initially, EG11598-MONOMER (MoeB) was presumed to catalyze transfer of sulfur atoms to CPLX0-2502 , however other evidence indicates that MoeB activates MoaD by adenylylation of MoaD's C-terminus. MoaD appears to further enhance MoeB's activation of G7325-MONOMER . Surface plasmon resonance studies suggested that IscS specifically binds to the putative in vivo MoeB-MoaD complex . It has since been determined that the carboxy-adenylated MoaD is sulfurated by the IscS via TusA or YnjE sulfurtransferases . Purified recombinant MoeB was shown to be a homodimer in solution . It was also shown to form a MoeB-MoaD heterotetrameric complex. Crystal structures of the apo, ATP-bound, and MoaD-adenylate forms of the MoeB-MoaD complex have been determined at 1.7, 2.9 and 2.1 Å resolution, respectively . The interaction between these proteins was also demonstrated in solution . MoaD structurally resembles the ubiquitin and ThiS proteins...

## Biological Role

Activated by fnr (protein.P0A9E5), modE (protein.P0A9G8), csrA (protein.P69913).

## Enriched Pathways

- `eco04122` Sulfur relay system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30748|protein.P30748]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=moaD; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=moaD; function=+
- `activates` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `C` - regulator=CsrA; target=moaD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002675,ECOCYC:EG11597,GeneID:945398`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:819048-819293:+; feature_type=gene
