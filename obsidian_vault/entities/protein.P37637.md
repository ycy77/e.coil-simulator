---
entity_id: "protein.P37637"
entity_type: "protein"
name: "mdtF"
source_database: "UniProt"
source_id: "P37637"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdtF yhiV b3514 JW3482"
---

# mdtF

`protein.P37637`

## Static

- Type: `protein`
- Source: `UniProt:P37637`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: Part of the tripartite efflux system MdtEF-TolC, which confers resistance to compounds such as rhodamine 6G, erythromycin, doxorubicin, ethidium bromide, TPP, SDS, deoxycholate, crystal violet and benzalkonium. {ECO:0000269|PubMed:11566977}. MdtF is the inner membrane subunit of a putative tripartite efflux complex; production of the complex (through expression of cloned mdtEF genes) confers some degree of resistance to various toxic compounds in laboratory strains of E. coli K-12 (see TRANS-CPLX-204 for more detail). MdtF can function with the AcrA membrane fusion protein for efflux of bile salts (cholate, taurocholate), dyes (crystal violet, ethidium bromide) and antibiotics (novobiocin, ciprofloxacin, eerythromycin) . mdtF expressed from a plasmid can complement the steroid hormone efflux deficient phenotype of a strain lacking both AcrB and EmrAB MdtF was isolated as a homotrimer in inner membrane vesicles purified from E. coli strain BL21 MdtF belongs to the Hydrophobe/Amphiphile Efflux-1 (HAE1) family of transporters within the resistance-nodulation-cell division (RND) superfamily . A ΔmdtF mutant shows increased persister cell formation under antibiotic stress . The mdtF Keio collection mutant (BW25113 ΔmdtF::kan) shows a significant increase in swimming motility...

## Biological Role

Component of multidrug efflux pump MdtEF-TolC (complex.ecocyc.TRANS-CPLX-204).

## Annotation

FUNCTION: Part of the tripartite efflux system MdtEF-TolC, which confers resistance to compounds such as rhodamine 6G, erythromycin, doxorubicin, ethidium bromide, TPP, SDS, deoxycholate, crystal violet and benzalkonium. {ECO:0000269|PubMed:11566977}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TRANS-CPLX-204|complex.ecocyc.TRANS-CPLX-204]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3514|gene.b3514]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37637`
- `KEGG:ecj:JW3482;eco:b3514;ecoc:C3026_19040;`
- `GeneID:948030;`
- `GO:GO:0005886; GO:0006855; GO:0009636; GO:0015125; GO:0015562; GO:0015721; GO:0016020; GO:0042802; GO:0042908; GO:0042910; GO:0046677`

## Notes

Multidrug resistance protein MdtF
