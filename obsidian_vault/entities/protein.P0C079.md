---
entity_id: "protein.P0C079"
entity_type: "protein"
name: "relB"
source_database: "UniProt"
source_id: "P0C079"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "relB b1564 JW1556"
---

# relB

`protein.P0C079`

## Static

- Type: `protein`
- Source: `UniProt:P0C079`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Counteracts the effect of cognate toxin RelE via direct protein-protein interaction, preventing RelE from entering the ribosome A site and thus inhibiting its endoribonuclease activity. An autorepressor of relBE operon transcription. 2 RelB dimers bind to 2 operator sequences; DNA-binding and repression is stronger when complexed with toxin/corepressor RelE by conditional cooperativity (PubMed:18501926, PubMed:22981948). Increased transcription rate of relBE and activation of relE is consistent with a lower level of RelB in starved cells due to degradation of RelB by protease Lon. {ECO:0000269|PubMed:11274135, ECO:0000269|PubMed:11717402, ECO:0000269|PubMed:12123459, ECO:0000269|PubMed:18501926, ECO:0000269|PubMed:18532983, ECO:0000269|PubMed:19707553, ECO:0000269|PubMed:19747491, ECO:0000269|PubMed:22210768, ECO:0000269|PubMed:22981948, ECO:0000269|PubMed:9767574}.; FUNCTION: Seems to be a principal mediator of cell death in liquid media. {ECO:0000269|PubMed:19707553}.

## Biological Role

Component of RelB-RelE antitoxin/toxin complex / DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-7791), Qin prophage; antitoxin/DNA-binding transcriptional repressor RelB (complex.ecocyc.CPLX0-7928).

## Annotation

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Counteracts the effect of cognate toxin RelE via direct protein-protein interaction, preventing RelE from entering the ribosome A site and thus inhibiting its endoribonuclease activity. An autorepressor of relBE operon transcription. 2 RelB dimers bind to 2 operator sequences; DNA-binding and repression is stronger when complexed with toxin/corepressor RelE by conditional cooperativity (PubMed:18501926, PubMed:22981948). Increased transcription rate of relBE and activation of relE is consistent with a lower level of RelB in starved cells due to degradation of RelB by protease Lon. {ECO:0000269|PubMed:11274135, ECO:0000269|PubMed:11717402, ECO:0000269|PubMed:12123459, ECO:0000269|PubMed:18501926, ECO:0000269|PubMed:18532983, ECO:0000269|PubMed:19707553, ECO:0000269|PubMed:19747491, ECO:0000269|PubMed:22210768, ECO:0000269|PubMed:22981948, ECO:0000269|PubMed:9767574}.; FUNCTION: Seems to be a principal mediator of cell death in liquid media. {ECO:0000269|PubMed:19707553}.

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7791|complex.ecocyc.CPLX0-7791]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `is_component_of` --> [[complex.ecocyc.CPLX0-7928|complex.ecocyc.CPLX0-7928]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `represses` --> [[gene.b1562|gene.b1562]] `RegulonDB` `C` - regulator=RelB; target=hokD; function=-
- `represses` --> [[gene.b1563|gene.b1563]] `RegulonDB` `S` - regulator=RelB; target=relE; function=-
- `represses` --> [[gene.b1564|gene.b1564]] `RegulonDB` `S` - regulator=RelB; target=relB; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1564|gene.b1564]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C079`
- `KEGG:ecj:JW1556;eco:b1564;ecoc:C3026_09025;`
- `GeneID:948308;98387559;99778183;`
- `GO:GO:0000976; GO:0001217; GO:0006351; GO:0006355; GO:0032993; GO:0040008; GO:0044010; GO:0097351; GO:0110001`

## Notes

Antitoxin RelB
