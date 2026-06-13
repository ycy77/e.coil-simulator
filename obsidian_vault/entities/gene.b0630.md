---
entity_id: "gene.b0630"
entity_type: "gene"
name: "lipB"
source_database: "NCBI RefSeq"
source_id: "gene-b0630"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0630"
  - "lipB"
---

# lipB

`gene.b0630`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0630`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lipB (gene.b0630) is a gene entity. It encodes lipB (protein.P60720). Encoded protein function: FUNCTION: Catalyzes the transfer of endogenously produced octanoic acid from octanoyl-acyl-carrier-protein onto the lipoyl domains of lipoate-dependent enzymes. Lipoyl-ACP can also act as a substrate although octanoyl-ACP is likely to be the physiological substrate. {ECO:0000255|HAMAP-Rule:MF_00013, ECO:0000269|PubMed:15642479, ECO:0000269|PubMed:16342964}. EcoCyc product frame: EG11591-MONOMER. EcoCyc synonyms: cde, lip. Genomic coordinates: 661637-662278. EcoCyc protein note: LipB is a lipoyl-/octanoyl-ACP:protein transferase that catalyzes the first step of de novo lipoate biosynthesis . In vitro, it transfers lipoyl or octanoyl domains from the corresponding acylated ACP to its target proteins; in vivo, octanoyl-ACP is the relevant substrate. Lipoate modification of the E2 subunits is important for the function of PYRUVATEDEH-CPLX , 2OXOGLUTARATEDEH-CPLX "α-ketoglutarate dehydrogenase" , and the GCVMULTI-CPLX . The LipB protein is translated from a TTG translation initiation codon ; protein translated from the downstream ATG is not active . The LipB-catalyzed reaction proceeds via an acyl-enzyme intermediate. The octanoate group is first transferred from the thiol of ACP to the C169 thiol of LipB, followed by transfer to a specific lysine residue of E2 subunits...

## Enriched Pathways

- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60720|protein.P60720]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002160,ECOCYC:EG11591,GeneID:945217`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:661637-662278:-; feature_type=gene
