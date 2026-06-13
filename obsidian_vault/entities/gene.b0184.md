---
entity_id: "gene.b0184"
entity_type: "gene"
name: "dnaE"
source_database: "NCBI RefSeq"
source_id: "gene-b0184"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0184"
  - "dnaE"
---

# dnaE

`gene.b0184`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0184`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dnaE (gene.b0184) is a gene entity. It encodes dnaE (protein.P10443). Encoded protein function: FUNCTION: DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria (PubMed:2932432). This DNA polymerase also exhibits 3' to 5' exonuclease activity. The alpha chain is the DNA polymerase catalytic subunit (PubMed:2932432). It is tethered to replicating DNA by the beta sliding clamp (dnaN), which confers extremely high processivity to the catalytic subunit, copying a 5.4 kb genome in 11 seconds, a speed of at least 500 nucleotides/second at 30 degrees Celsius (PubMed:2413035). {ECO:0000269|PubMed:2413035, ECO:0000269|PubMed:2932432}. EcoCyc product frame: EG10238-MONOMER. EcoCyc synonyms: sdgC, polC. Genomic coordinates: 205126-208608. EcoCyc protein note: The alpha subunit of DNA polymerase III catalyzes the polymerase activity of the holoenzyme complex . Replicative 5' to 3' polymerization of DNA requires dNTPs and template DNA with a bound RNA primer . The newly polymerized DNA is covalently attached to the RNA primer . The presence of the epsilon subunit increases the polymerase activity of the alpha subunit two-fold . The alpha subunit is required for misincorporation and bypass during UV mutagenesis . The middle portion of the alpha subunit (residues 542-991) is involved in binding to the polymerase III beta subunit...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P10443|protein.P10443]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=dnaE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000624,ECOCYC:EG10238,GeneID:944877`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:205126-208608:+; feature_type=gene
