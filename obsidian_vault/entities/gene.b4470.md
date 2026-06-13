---
entity_id: "gene.b4470"
entity_type: "gene"
name: "cyuA"
source_database: "NCBI RefSeq"
source_id: "gene-b4470"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4470"
  - "cyuA"
---

# cyuA

`gene.b4470`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4470`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cyuA (gene.b4470) is a gene entity. It encodes yhaM (protein.P42626). Encoded protein function: FUNCTION: Plays a role in L-cysteine detoxification; it has been speculated to be a cysteine desulfhydrase (PubMed:27435271). {ECO:0000303|PubMed:27435271}. EcoCyc product frame: G7622-MONOMER. EcoCyc synonyms: b3109, yhaN, b3108, yhaM. Genomic coordinates: 3255341-3256651. EcoCyc protein note: CyuA is an EC-4.4.1.28 in E. coli K-12. It is the major anaerobic cysteine-catabolizing enzyme . Contrary to earlier reports, the enzyme does not act in L-cysteine detoxification; rather, together with YHAO-MONOMER the enzyme allows the organism to utilize L-cysteine as the sole nitrogen and carbon/energy source . CyuA shares sequence similarity with dehydratases that have an iron-sulfur (Fe-S) cluster, such as CyuA in TAX-2190, but exhibits higher sensitivity to molecular oxygen exposure. Activity of CyuA purified in an anaerobic chamber was restored when incubated with Fe(II) and dithiothreitol (DTT), a treatment used with dehydratases to reactivate damaged Fe-S clusters . The enzyme is highly specific, and D-cysteine and analogs of L-cysteine are not substrates. In competition studies in vitro, CyuA was found to bind compounds that contained both a thiol and a primary amine group; serine, alanine, leucine, glutathione nor Β-mercaptoethanol are unable to inhibit...

## Biological Role

Activated by decR (protein.P0ACJ5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42626|protein.P42626]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ5|protein.P0ACJ5]] `RegulonDB` `S` - regulator=DecR; target=cyuA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0174100,ECOCYC:G7622,GeneID:2847723`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3255341-3256651:-; feature_type=gene
