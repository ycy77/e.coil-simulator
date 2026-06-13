---
entity_id: "gene.b4367"
entity_type: "gene"
name: "fhuF"
source_database: "NCBI RefSeq"
source_id: "gene-b4367"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4367"
  - "fhuF"
---

# fhuF

`gene.b4367`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4367`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fhuF (gene.b4367) is a gene entity. It encodes fhuF (protein.P39405). Encoded protein function: FUNCTION: Siderophore-iron reductase which is involved in iron removal from the hydroxamate-type siderophores coprogen, ferrichrome and ferrioxamine B after their transport into the cell (PubMed:14756576). Binds both the iron-loaded and the apo forms of ferrichrome (PubMed:33559753). {ECO:0000269|PubMed:14756576, ECO:0000269|PubMed:33559753}. EcoCyc product frame: G7949-MONOMER. EcoCyc synonyms: yjjS. Genomic coordinates: 4604875-4605663. EcoCyc protein note: FhuF is a ferric-siderophore reductase that is able to mobilize iron from ferrioxamine B, ferrichrome and coprogen . FhuF contains a 2Fe-2S iron sulfur cluster . Residues C244, C245, C256, and C259 are involved in coordination of the cluster and are required for protein function. The Cys-Cys-Xaa10-Cys-Xaa2-Cys motif is unusual among 2Fe-2S proteins . Purified FhuF can directly reduce ferrioxamine B-bound ferric ions in vitro. The reduced ferrous ion is not bound to the [2Fe-2S] cluster. The system that regenerates reduced FhuF is not known . His-tagged FhuF has been overproduced and purified and structurally characterized by small-angle X-ray scattering and paramagnetic NMR spectroscopy . The reduction potential of FhuF has been measured and was found to be pH-dependent . In a sufD mutant, the FhuF protein is unstable...

## Biological Role

Repressed by fur (protein.P0A9A9), oxyR (protein.P0ACQ4), nac (protein.Q47005). Activated by ygaV (protein.P77295).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39405|protein.P39405]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P77295|protein.P77295]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=fhuF; function=-
- `represses` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=fhuF; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=fhuF; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0014326,ECOCYC:G7949,GeneID:948891`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4604875-4605663:-; feature_type=gene
