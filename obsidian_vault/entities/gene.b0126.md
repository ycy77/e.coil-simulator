---
entity_id: "gene.b0126"
entity_type: "gene"
name: "can"
source_database: "NCBI RefSeq"
source_id: "gene-b0126"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0126"
  - "can"
---

# can

`gene.b0126`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0126`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

can (gene.b0126) is a gene entity. It encodes can (protein.P61517). Encoded protein function: Carbonic anhydrase 2 (EC 4.2.1.1) (Carbonate dehydratase 2) EcoCyc product frame: EG12319-MONOMER. EcoCyc synonyms: yadF. Genomic coordinates: 142008-142670. EcoCyc protein note: E. coli encodes two carbonic anhydrases, CynT (CARBODEHYDRAT-MONOMER) and Can (carbonic anhydrase 2). The enzymes belong to Clade A and Clade B of the β class of carbonic anhydrases, respectively . Carbonic anhydrase 2 is essential for growth at amospheric pCO2 . Enzymatic activity of carbonic anhydrase 2 is pH-dependent . Inhibition of Can activity by sulfonamides and various clinically used drugs has been investigated . Crystal structures of carbonic anhydrase 2 have been solved. The crystal structure data as well as size exclusion chromatography indicate that the protein exists as a homotetramer in solution . There is structural evidence for a noncatalytic binding site for bicarbonate . A can mutant does not grow under normal atmospheric conditions, but the mutant can grow under conditions with a high exogenous or endogenous supply of CO2. Expression of cynT suppresses phenotypes of a can mutant . A can cynT double mutant is only viable under high CO2 conditions . Expression of can is inversely proportional to the growth rate and does not depend on CO2 levels...

## Biological Role

Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P61517|protein.P61517]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=can; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=can; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000442,ECOCYC:EG12319,GeneID:944832`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:142008-142670:-; feature_type=gene
