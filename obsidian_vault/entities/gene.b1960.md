---
entity_id: "gene.b1960"
entity_type: "gene"
name: "vsr"
source_database: "NCBI RefSeq"
source_id: "gene-b1960"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1960"
  - "vsr"
---

# vsr

`gene.b1960`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1960`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

vsr (gene.b1960) is a gene entity. It encodes vsr (protein.P09184). Encoded protein function: FUNCTION: Deamination of 5-methylcytosine in DNA results in T/G mismatches. If unrepaired, these mismatches can lead to C-to-T transition mutations. The very short patch (VSP) repair process in E.coli counteracts the mutagenic process by repairing the mismatches in favor of the G-containing strand. This enzyme is an endonuclease that nicks double-stranded DNA within the sequence CT(AT)GN or NT(AT)GG next to the thymidine residue that is mismatched to 2'-deoxyguanosine. The incision is mismatch-dependent and strand-specific. {ECO:0000269|PubMed:10871403, ECO:0000269|PubMed:1944537}. EcoCyc product frame: EG11068-MONOMER. Genomic coordinates: 2030448-2030918. EcoCyc protein note: Vsr is an endonuclease that specifically recognizes and exhibits strand-specific nicking at T:G DNA mismatches, which arise from spontaneous deamination at 5-methylcytosine, the product of Dcm (cytosine) methylation . Vsr activity counterbalances the mutagenesis associated with dcm activity . Vsr is an essential component of the very short patch (VSP) mismatch repair pathway, as is PolA , whereas MutL and MutS are involved but not essential . A minimal VSP pathway containing the purified components Vsr, PolA, DNA ligase I (LigA) and a plasmid substrate has been reconstituted in vitro...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09184|protein.P09184]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006507,ECOCYC:EG11068,GeneID:946476`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2030448-2030918:-; feature_type=gene
