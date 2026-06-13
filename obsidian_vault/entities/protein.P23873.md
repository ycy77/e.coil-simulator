---
entity_id: "protein.P23873"
entity_type: "protein"
name: "hipB"
source_database: "UniProt"
source_id: "P23873"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hipB b1508 JW1501"
---

# hipB

`protein.P23873`

## Static

- Type: `protein`
- Source: `UniProt:P23873`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Neutralizes the toxic effect of cognate toxin HipA (PubMed:20616060). Also neutralizes the toxic effect of non-cognate toxin YjjJ (PubMed:28430938). Binds to operator sites with the consensus sequence 5-'TATCCN(8)GGATA-3' to repress the hipBA operon promoter (PubMed:8021189, PubMed:19150849); binding of HipB(2) to DNA induces a 70 degree bend (PubMed:19150849). This forces HipA dimerization, which blocks HipA's active site and thus its toxic action (PubMed:26222023). May play a role in biofilm formation (PubMed:23329678). {ECO:0000269|PubMed:19150849, ECO:0000269|PubMed:20616060, ECO:0000269|PubMed:23329678, ECO:0000269|PubMed:26222023, ECO:0000269|PubMed:28430938, ECO:0000269|PubMed:8021189}. HipB is a transcriptional repressor that functions as the antagonist of HipA, which was the first protein found to mediate the phenomenon of persistence in E. coli. A small fraction of cells within a population are dormant persister cells; these cells are phenotypic variants that are not killed by antibiotics, leading to multidrug tolerance (MDT). Persistence may be ultimately due to global remodeling of the persister cell's ribosomes . The HipAB system can be categorized as a type II toxin/antitoxin module. In the absence of its binding partner HipB, HipA is toxic to the cell...

## Biological Role

Component of HipAB toxin/antitoxin complex / DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-7425), HipB antitoxin / DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-7757).

## Annotation

FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Neutralizes the toxic effect of cognate toxin HipA (PubMed:20616060). Also neutralizes the toxic effect of non-cognate toxin YjjJ (PubMed:28430938). Binds to operator sites with the consensus sequence 5-'TATCCN(8)GGATA-3' to repress the hipBA operon promoter (PubMed:8021189, PubMed:19150849); binding of HipB(2) to DNA induces a 70 degree bend (PubMed:19150849). This forces HipA dimerization, which blocks HipA's active site and thus its toxic action (PubMed:26222023). May play a role in biofilm formation (PubMed:23329678). {ECO:0000269|PubMed:19150849, ECO:0000269|PubMed:20616060, ECO:0000269|PubMed:23329678, ECO:0000269|PubMed:26222023, ECO:0000269|PubMed:28430938, ECO:0000269|PubMed:8021189}.

## Outgoing Edges (10)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7425|complex.ecocyc.CPLX0-7425]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7757|complex.ecocyc.CPLX0-7757]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b1507|gene.b1507]] `RegulonDB` `S` - regulator=HipB; target=hipA; function=-
- `represses` --> [[gene.b1508|gene.b1508]] `RegulonDB` `S` - regulator=HipB; target=hipB; function=-
- `represses` --> [[gene.b2451|gene.b2451]] `RegulonDB` `S` - regulator=HipB; target=eutA; function=-
- `represses` --> [[gene.b2452|gene.b2452]] `RegulonDB` `S` - regulator=HipB; target=eutH; function=-
- `represses` --> [[gene.b2782|gene.b2782]] `RegulonDB` `S` - regulator=HipB; target=mazF; function=-
- `represses` --> [[gene.b2783|gene.b2783]] `RegulonDB` `S` - regulator=HipB; target=mazE; function=-
- `represses` --> [[gene.b2784|gene.b2784]] `RegulonDB` `S` - regulator=HipB; target=relA; function=-
- `represses` --> [[gene.b3081|gene.b3081]] `RegulonDB` `S` - regulator=HipB; target=fadH; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1508|gene.b1508]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23873`
- `KEGG:ecj:JW1501;eco:b1508;ecoc:C3026_08725;`
- `GeneID:946065;`
- `GO:GO:0000976; GO:0001046; GO:0001217; GO:0006351; GO:0006355; GO:0032993; GO:0040008; GO:0042803; GO:0043565; GO:0045892; GO:0110001`

## Notes

Antitoxin HipB
