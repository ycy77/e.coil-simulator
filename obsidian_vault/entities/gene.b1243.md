---
entity_id: "gene.b1243"
entity_type: "gene"
name: "oppA"
source_database: "NCBI RefSeq"
source_id: "gene-b1243"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1243"
  - "oppA"
---

# oppA

`gene.b1243`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1243`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

oppA (gene.b1243) is a gene entity. It encodes oppA (protein.P23843). Encoded protein function: FUNCTION: Part of the ABC transporter complex OppABCDF involved in the uptake of oligopeptides (PubMed:2187863). Plays an important nutritional role (Probable). Binds peptides containing from two to five amino acid residues (PubMed:21983341, PubMed:3536860). Displays a preference for tripeptides and tetrapeptides over dipeptides and pentapeptides, for peptides composed of L-amino acids and for positively charged peptides (PubMed:21983341, PubMed:3536860). Cannot bind the cell wall peptide L-Ala-D-Gly-gamma-meso-diaminopimelic acid (PubMed:21705338). {ECO:0000269|PubMed:21705338, ECO:0000269|PubMed:2187863, ECO:0000269|PubMed:21983341, ECO:0000269|PubMed:3536860, ECO:0000305}. EcoCyc product frame: OPPA-MONOMER. Genomic coordinates: 1301182-1302813. EcoCyc protein note: OppA is the periplasmic binding protein of an ABC transporter that mediates the high affinity uptake of oligopeptides. The crystal structure of OppA complexed with peptide ligand (modeled using a tripeptide) is highly similar to that of the well characterized S. typhimurium OppA (see ); the ligand is bound in a closed cavity deep inside the protein; the binding cavity contains large hydrated pockets believed to allow the presence of chemically diverse peptide side chains...

## Biological Role

Repressed by Hfq (complex.ecocyc.CPLX0-1461), fur (protein.P0A9A9), arcA (protein.P0A9Q1), lrp (protein.P0ACJ0). Activated by arcA (protein.P0A9Q1), nac (protein.Q47005).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23843|protein.P23843]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=oppA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=oppA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-1461|complex.ecocyc.CPLX0-1461]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=oppA; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=oppA; function=-+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=oppA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004172,ECOCYC:EG10674,GeneID:945830`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1301182-1302813:+; feature_type=gene
