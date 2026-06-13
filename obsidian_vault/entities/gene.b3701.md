---
entity_id: "gene.b3701"
entity_type: "gene"
name: "dnaN"
source_database: "NCBI RefSeq"
source_id: "gene-b3701"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3701"
  - "dnaN"
---

# dnaN

`gene.b3701`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3701`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dnaN (gene.b3701) is a gene entity. It encodes dnaN (protein.P0A988). Encoded protein function: FUNCTION: Confers DNA tethering and processivity to DNA polymerases and other proteins. Acts as a clamp, forming a ring around DNA (a reaction catalyzed by the clamp-loading complex) which diffuses in an ATP-independent manner freely and bidirectionally along dsDNA (PubMed:2040637). DNA bound in the ring is bent 22 degrees, in solution primed DNA is bound more tightly than dsDNA, suggesting the clamp binds both ss- and dsDNA (PubMed:18191219). In a complex of DNA with this protein, alpha, epsilon and tau subunits however the DNA is only slightly bent (PubMed:26499492). Coordinates protein traffic at the replication fork, where it interacts with multiple DNA polymerases, repair factors and other proteins (PubMed:14592985, PubMed:14729336, PubMed:15466025, PubMed:15952889, PubMed:16168375, PubMed:22716942, PubMed:26499492). Initially characterized for its ability to contact the alpha subunit (dnaE) of DNA polymerase III (Pol III), tethering it to the DNA and conferring very high processivity (PubMed:2040637). Pol III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria; it also exhibits 3'-5' exonuclease proofreading activity...

## Biological Role

Repressed by dnaA (protein.P03004), fis (protein.P0A6R3). Activated by rpoD (protein.P00579), dnaA (protein.P03004), argP (protein.P0A8S1), rpoS (protein.P13445).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A988|protein.P0A988]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dnaN; function=+
- `activates` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `C` - regulator=DnaA; target=dnaN; function=-+
- `activates` <-- [[protein.P0A8S1|protein.P0A8S1]] `RegulonDB` `S` - regulator=ArgP; target=dnaN; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=dnaN; function=+
- `represses` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `C` - regulator=DnaA; target=dnaN; function=-+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=dnaN; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012098,ECOCYC:EG10242,GeneID:948218`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3881221-3882321:-; feature_type=gene
