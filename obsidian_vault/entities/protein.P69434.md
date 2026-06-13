---
entity_id: "protein.P69434"
entity_type: "protein"
name: "pgaA"
source_database: "UniProt"
source_id: "P69434"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305|PubMed:18359807}; Multi-pass membrane protein {ECO:0000305|PubMed:18359807}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pgaA ycdS b1024 JW1010"
---

# pgaA

`protein.P69434`

## Static

- Type: `protein`
- Source: `UniProt:P69434`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305|PubMed:18359807}; Multi-pass membrane protein {ECO:0000305|PubMed:18359807}.

## Enriched Summary

FUNCTION: Exports the biofilm adhesin polysaccharide poly-beta-1,6-N-acetyl-D-glucosamine (PGA) across the outer membrane. The PGA transported seems to be partially N-deacetylated since N-deacetylation of PGA by PgaB is needed for PGA export through the PgaA porin.; FUNCTION: Required for the synthesis of the beta-1,6-GlcNAc polysaccharide (PGA or poly-GlcNAc) that seems to serve as a biofilm adhesin. The pgaABCD locus is required for the synthesis of a cell-bound hexosamine-rich polysaccharide, which was identified as a linear polymer of β-1,6-N-acetylglucosamine residues (PGA), an adhesin essential in biofilm formation . PgaA exports PGA across the outer membrane. N-deacetylation of PGA by PgaB promotes its transport across the outer membrane. A pgaA mutant has reduced biofilm formation . pgaA mutants do not release significant amounts of PGA into the medium during shaking compared to wild-type . PGA from pgaA mutants is not externally exposed, showing PgaA is involved in transport of PGA across the outer membrane . Expression of pgaABCD is higher at 37°C than at 21°C and is highest during stationary phase . Expression increased in response to 1% NaCl or ethanol . Expression increased in response to glucose, ethanol, NaCl, and MnCl2 in a clinical isolate, and dramatically increased upon deletion or mutation of csrA in this strain...

## Biological Role

Catalyzes TRANS-RXN0-275 (reaction.ecocyc.TRANS-RXN0-275).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Exports the biofilm adhesin polysaccharide poly-beta-1,6-N-acetyl-D-glucosamine (PGA) across the outer membrane. The PGA transported seems to be partially N-deacetylated since N-deacetylation of PGA by PgaB is needed for PGA export through the PgaA porin.; FUNCTION: Required for the synthesis of the beta-1,6-GlcNAc polysaccharide (PGA or poly-GlcNAc) that seems to serve as a biofilm adhesin.

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-275|reaction.ecocyc.TRANS-RXN0-275]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1024|gene.b1024]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69434`
- `KEGG:ecj:JW1010;eco:b1024;ecoc:C3026_06225;`
- `GeneID:945596;`
- `GO:GO:0009279; GO:0015159; GO:0015774; GO:0044010; GO:1901515`

## Notes

Poly-beta-1,6-N-acetyl-D-glucosamine export protein (PGA export protein) (Poly-beta-1,6-GlcNAc export protein)
